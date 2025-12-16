# autofilemover

A simple tool to automatically monitor and move specified types of files from a source directory to a destination directory.

## Features
- Real-time monitoring of source directory and its subdirectories
- Automatic file movement with conflict handling (renames files with the same name)
- Customizable file extensions to monitor (supports any file type)
- Easy configuration via a text file
- Lightweight and runs in the background

## Download
You can download the precompiled executable file from the [Releases](https://github.com/yourusername/autofilemover/releases) section. No installation required - just run the .exe file.

## Usage Guide

### 1. First Run
When you run the program for the first time:
- A `path.txt` configuration file will be automatically created in the same directory as the executable
- The program will prompt you to edit this file before restarting

### 2. Configure path.txt
Open `path.txt` with a text editor and set the following parameters:

> First line: Source directory to monitor (absolute path)
/path/to/your/source/directory


> Second line: Destination directory for moved files (absolute path)
/path/to/your/destination/directory


> Third line: Supported file extensions (comma-separated)
.mp4, .txt, .pdf, .jpg # Customize according to your needs


### 3. Run the Program
- Double-click the executable file
- The monitoring service will start and run in the background
- Press `Ctrl+C` in the console window to stop the service

## Notes
- The program waits 0.5 seconds before moving files to ensure they're fully written
- Subdirectories of the source directory are monitored recursively
- If a file with the same name exists in the destination, it will be renamed (e.g., `document.txt` → `document_1.txt`)
- All configuration changes require a program restart to take effect

---

# autofilemover（文件自动移动工具）

一个简单的工具，用于自动监控并移动源目录中指定类型的文件到目标目录。

## 功能特点
- 实时监控源目录及其子目录
- 自动移动文件并处理同名冲突（自动重命名文件）
- 可自定义监控的文件扩展名（支持任何文件类型）
- 通过文本文件轻松配置
- 轻量且在后台运行

## 下载
您可以从[发布页面](https://github.com/yourusername/autofilemover/releases)下载预编译的可执行文件。无需安装，直接运行.exe文件即可。

## 使用指南

### 1. 首次运行
首次运行程序时：
- 会在可执行文件所在目录自动创建`path.txt`配置文件
- 程序会提示您编辑此文件后重新启动

### 2. 配置path.txt
使用文本编辑器打开`path.txt`，设置以下参数：

> 第一行：要监控的源目录（绝对路径）
C:/path/to/your/source/directory


> 第二行：文件要移动到的目标目录（绝对路径）
D:/path/to/your/destination/directory


> 第三行：支持的文件扩展名（用逗号分隔）
.mp4, .txt, .pdf, .jpg # 根据您的需求自定义


### 3. 运行程序
- 双击可执行文件
- 监控服务将启动并在后台运行
- 在控制台窗口中按`Ctrl+C`停止服务

## 注意事项
- 程序会等待0.5秒再移动文件，以确保文件已完全写入
- 源目录的子目录会被递归监控
- 如果目标目录中存在同名文件，将自动重命名（例如`document.txt` → `document_1.txt`）
- 所有配置更改需要重启程序才能生效