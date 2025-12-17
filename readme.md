# autofilemover

A simple tool to automatically monitor and move specified types of files from a source directory to a destination directory.

## Features
- **Real-time Monitoring**: Automatically scans the source directory and all its subdirectories.
- **Conflict Handling**: If a file with the same name exists in the destination, it is automatically renamed (e.g., `video.mp4` → `video_1.mp4`).
- **Quick Folder Access**: Press `F` while the console window is active to instantly open the destination directory in Windows File Explorer.
- **Operation Logging**: Displays precise timestamps and the source/destination paths for every moved file.
- **Data Tracking**: Shows the cumulative size (in GB) of all files moved during the current session.
- **Flexible Configuration**: Easily customize paths and supported file extensions via a simple text file.

## Download
You can download the precompiled executable file from the Releases page. No installation required—just run the `.exe` file.

## Usage Guide

### 1. First Run
When you run the program for the first time:
- A `path.txt` configuration file will be automatically created in the same folder as the executable.
- The program will display a prompt and wait for you to edit this file before exiting.

### 2. Configure path.txt
Open `path.txt` with any text editor and set the following parameters (Example for Windows):

> **Line 1**: The source directory you want to monitor.
> `C:\Users\YourName\Downloads\Source`
> 
> **Line 2**: The destination directory where files should be moved.
> `D:\MyFile\Organized`
> 
> **Line 3**: Supported file extensions, separated by commas.
> `.mp4, .txt, .pdf, .jpg`

### 3. Run the Program
- Double-click the executable to start the service.
- **Active Window Shortcuts**:
    - **`F`**: Open the Destination Directory (works only when the program window is in focus).
    - **`Ctrl+C`**: Safely stop the monitoring service.

## Notes
- **Delay**: The program waits 0.5 seconds before moving a file to ensure it has finished writing to the disk.
- **Scope**: Monitoring is recursive, meaning files inside subdirectories of the source folder will also be moved.
- **Session Data**: The cumulative data size counter resets to 0.00 GB whenever the program is restarted.

---

# autofilemover（文件自动移动工具）

一个简单的工具，用于自动监控并移动源目录中指定类型的文件到目标目录。

## 功能特点
- **实时监控**：自动扫描源目录及其所有子目录。
- **冲突处理**：如果目标目录存在同名文件，程序会自动重命名（例如 `video.mp4` 变为 `video_1.mp4`）。
- **快捷访问**：当控制台窗口处于激活状态时，按 `F` 键可立即打开目标文件夹。
- **详细日志**：每次移动文件时，都会显示具体的时间戳和路径信息。
- **数据统计**：实时显示当前运行周期内累计移动的文件总大小（单位：GB）。
- **轻松配置**：通过简单的 `path.txt` 文件即可自定义路径和支持的文件类型。

## 下载
您可以从发布页面下载预编译的可执行文件。无需安装，直接运行 `.exe` 文件即可。

## 使用指南

### 1. 首次运行
首次运行程序时：
- 会在可执行文件所在目录自动创建 `path.txt` 配置文件。
- 程序会提示您编辑此文件，并在按回车键后退出，方便您进行配置。

### 2. 配置 path.txt
使用文本编辑器打开 `path.txt`，按顺序设置以下参数（Windows 路径示例）：

> **第一行**：要监控的源目录（绝对路径）。
> `C:\Users\用户名\Downloads\监控文件夹`
> 
> **第二行**：文件要移动到的目标目录（绝对路径）。
> `E:\库\已整理`
> 
> **第三行**：支持的文件扩展名，用逗号分隔。
> `.mp4, .txt, .pdf, .jpg`

### 3. 运行程序
- 双击运行程序。
- **窗口激活时的快捷键**：
    - **`F` 键**：在资源管理器中快速打开目标目录。
    - **`Ctrl+C`**：停止监控服务并退出程序。

## 注意事项
- **写入延迟**：程序检测到文件后会等待 0.5 秒再执行移动，以确保文件已完全写入磁盘。
- **递归监控**：源目录下的所有子文件夹都在监控范围内。
- **数据清零**：累计移动的文件大小统计会在程序重启后清零。