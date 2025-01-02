# FileMate

FileMate 是一个智能文件管理分类软件，旨在帮助用户自动整理和分类电脑中的文件，提高工作效率。

## 功能特点

- **智能分类**：利用先进的机器学习算法，自动识别文件类型并进行分类。
- **用户自定义规则**：允许用户根据自己的需求设置分类规则。
- **图形用户界面**：提供直观的图形界面，方便用户操作。
- **命令行界面**：为高级用户提供命令行工具，快速执行文件管理任务。
- **跨平台支持**：支持 Windows、macOS 和 Linux 操作系统。

## 安装

### 通过 pip 安装

```bash
pip install filemate
```
### 从源代码安装
1. 克隆仓库：
  ```bash
  git clone https://github.com/yourusername/FileMate.git
  ```
2. 进入项目目录：
  ```bash
  cd FileMate
  ```
3. 安装依赖：
  ```bash
  pip install -r requirements.txt
  ```
4. 安装 FileMate：
  ```bash
  python setup.py install
  ```
## 使用
### 图形用户界面
启动 FileMate 的图形界面：

```bash
filemate_gui
```
### 命令行界面
使用 FileMate 的命令行工具：

```bash
filemate --help
```
### 配置
FileMate 允许用户在 config.json 文件中自定义分类规则。

```json
{
  "rules": [
    {
      "extension": ".txt",
      "folder": "Text Files"
    },
    {
      "extension": ".jpg",
      "folder": "Images"
    }
  ]
}
```
## 开发
### 运行测试
```bash
python -m unittest discover -s tests -p 'test_*.py'
```
## 贡献
欢迎贡献！请阅读 CONTRIBUTING.md 了解如何为项目做贡献。

## 文档
项目文档位于 docs 目录。

## 许可证
FileMate 采用 MIT 许可证。

## 联系
项目主页：https://github.com/waltert812/FileMate
问题跟踪：https://github.com/waltert812/FileMate/issues