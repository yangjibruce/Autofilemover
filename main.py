import os
import sys
import time
import shutil
from datetime import datetime  # 仅新增此行
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- 外部配置文件名 ---
CONFIG_FILE = "path.txt"

# -------------------------- 配置参数（不变动）--------------------------
DELAY_SECONDS = 0.5
# ----------------------------------------------------------------------

# 默认配置内容
DEFAULT_SOURCE_DIR = "/path/to/your/VideoSource"
DEFAULT_DEST_DIR = "/path/to/your/VideoDestination"
DEFAULT_EXTENSIONS = ".mp4, .mkv, .avi"

DEFAULT_CONFIG_CONTENT = f"""# ----------------------------------------------------------------------
# 文件整理监控配置：path.txt
# 请将下方 /path/to/your/ 替换为您电脑上的实际绝对路径！
# ----------------------------------------------------------------------

# 第一行：【必填】要监控的源目录（SOURCE_DIR），程序将实时扫描此目录及其子目录。
{DEFAULT_SOURCE_DIR}

# 第二行：【必填】文件最终要移动到的目标目录（DEST_DIR）。
{DEFAULT_DEST_DIR}

# 第三行：【必填】支持的文件扩展名列表，使用逗号 (,) 分隔。
# 格式：可以带或不带点号，程序会自动转为小写。
{DEFAULT_EXTENSIONS}
"""

# 全局变量用于存储从文件中加载的配置
SOURCE_DIR = None
DEST_DIR = None
SUPPORTED_EXTENSIONS = ()
TOTAL_MOVED_SIZE = 0.0  # 新增：累计移动大小（字节）


def load_paths_from_file():
    """从 path.txt 文件中读取配置，如果不存在则创建默认文件"""
    global SOURCE_DIR
    global DEST_DIR
    global SUPPORTED_EXTENSIONS

    # 1. 确定配置文件的完整路径
    try:
        # 兼容脚本和 PyInstaller 打包后的 .exe
        base_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, CONFIG_FILE)
    except Exception:
        config_path = CONFIG_FILE

    # 2. 检查配置文件是否存在
    if not os.path.exists(config_path):
        # 配置文件不存在，自动创建默认文件
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                f.write(DEFAULT_CONFIG_CONTENT)
            
            print("-" * 50)
            print(f"警告：配置文件 {CONFIG_FILE} 不存在。")
            print(f"已在以下路径自动创建默认文件：{config_path}")
            print("\n--------------------------------------------------")
            print("请编辑此文件，将示例路径替换为您的实际目录后，重新运行程序。")
            print("--------------------------------------------------")
            
            # 关键修改：暂停程序，等待用户输入，让用户看清提示
            input("\n按 Enter 键退出程序（请务必修改 path.txt 后再启动）...")
            sys.exit(1) # 退出程序，等待用户配置
            
        except Exception as e:
            print(f"错误：无法创建配置文件 {CONFIG_FILE}：{str(e)}")
            input("\n按 Enter 键退出程序...")
            sys.exit(1)

    # 3. 配置文件存在，开始读取
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            if len(lines) < 3:
                print(f"错误：配置文件 {CONFIG_FILE} 格式不正确。至少需要三行配置。")
                input("\n按 Enter 键退出程序...")
                sys.exit(1)
                
            SOURCE_DIR = lines[0]
            DEST_DIR = lines[1]
            
            extensions_str = lines[2].lower()
            extensions_list = [ext.strip() for ext in extensions_str.split(',') if ext.strip()]
            
            SUPPORTED_EXTENSIONS = tuple(
                ext if ext.startswith('.') else '.' + ext 
                for ext in extensions_list
            )

            print(f"从 {CONFIG_FILE} 加载配置成功。")
            
    except Exception as e:
        print(f"错误：读取配置文件 {CONFIG_FILE} 时发生错误：{str(e)}")
        input("\n按 Enter 键退出程序...")
        sys.exit(1)


class VideoFileHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        """当文件/目录被创建时触发"""
        if event.is_directory:
            return

        file_path = event.src_path
        file_ext = os.path.splitext(file_path)[1].lower()

        if file_ext in SUPPORTED_EXTENSIONS:
            time.sleep(DELAY_SECONDS)
            self.move_video_file(file_path)

    def on_moved(self, event):
        """当文件或目录被移动或重命名时触发"""
        if event.is_directory:
            return

        dest_path = event.dest_path
        dest_file_ext = os.path.splitext(dest_path)[1].lower()

        if dest_file_ext in SUPPORTED_EXTENSIONS:
            time.sleep(DELAY_SECONDS)
            self.move_video_file(dest_path)
            
    def move_video_file(self, file_path):
        """
        移动文件到目标目录，处理同名文件冲突
        """
        global TOTAL_MOVED_SIZE # 新增：引用全局变量
        if not DEST_DIR:
            print("目标目录未初始化！程序异常。")
            return

        # 移动前记录文件大小
        try:
            file_size = os.path.getsize(file_path)
        except:
            file_size = 0

        file_name = os.path.basename(file_path)
        dest_file_path = os.path.join(DEST_DIR, file_name)

        # 处理同名文件
        counter = 1
        while os.path.exists(dest_file_path):
            name, ext = os.path.splitext(file_name)
            dest_file_path = os.path.join(DEST_DIR, f"{name}_{counter}{ext}")
            counter += 1

        try:
            shutil.move(file_path, dest_file_path)
            # --- 以下为新增的逻辑 ---
            TOTAL_MOVED_SIZE += file_size
            total_gb = TOTAL_MOVED_SIZE / (1024**3)
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}] 成功移动文件：{file_path} -> {dest_file_path}")
            print(f" >> 本次运行累计移动：{total_gb:.2f} GB")
            # -----------------------
        except PermissionError:
            print(f"移动失败：无权限访问文件 {file_path}")
        except FileNotFoundError:
            print(f"移动失败：文件 {file_path} 已被删除或不存在")
        except Exception as e:
            print(f"移动失败：{file_path}，错误信息：{str(e)}")


def main():
    
    # 1. 加载路径配置和扩展名
    load_paths_from_file() 
    
    # 2. 检查源目录和扩展名列表是否有效
    if not SOURCE_DIR or not os.path.isdir(SOURCE_DIR):
        print(f"错误：源目录 {SOURCE_DIR} 不存在或未配置。")
        input("\n按 Enter 键退出程序...") # 路径配置错误也暂停
        sys.exit(1)

    if not SUPPORTED_EXTENSIONS:
        print("错误：未在 path.txt 中配置任何支持的文件扩展名。")
        input("\n按 Enter 键退出程序...") # 扩展名配置错误也暂停
        sys.exit(1)

    # 3. 创建目标目录（如果不存在）
    os.makedirs(DEST_DIR, exist_ok=True)
    
    # 4. 创建事件处理器和观察者
    event_handler = VideoFileHandler()
    observer = Observer()

    # 配置观察者：监控源目录，递归监控子文件夹
    observer.schedule(event_handler, path=SOURCE_DIR, recursive=True)

    # 5. 启动观察者
    observer.start()
    print("-" * 30)
    print(f"监控服务已启动。")
    print(f"正在监控：{SOURCE_DIR} (包括子目录)")
    print(f"文件将移动到：{DEST_DIR}")
    print(f"监控类型：{', '.join(SUPPORTED_EXTENSIONS)}")
    print("-" * 30)
    print("按 Ctrl+C 停止监控")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n正在停止监控...")

    observer.join()
    print("监控已停止")

if __name__ == "__main__":
    main()