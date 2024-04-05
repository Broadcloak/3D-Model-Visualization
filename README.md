# 三维模型可视化程序

这个程序实现了一个简单的三维模型可视化窗口，基于PyQt5、OpenGL和Open3D库，可以加载和显示PLY格式的三维模型文件。

## 配置文件信息

### 程序依赖

- Python 3.6+
- PyQt5
- OpenGL (PyOpenGL)
- open3d

### 使用方法

1. 运行程序
2. 点击菜单中的 "文件" -> "导入模型文件",在文件对话框中选择一个PLY格式的三维模型文件。
3. 程序加载并显示所选的三维模型文件，可通过鼠标调整模型的方向和缩放大小。

## 文件结构

- main.py: 主程序代码
- README.md: 说明文档
- models: 存放3维模型文件的目录（ply类型）

## 注意事项

- 确保安装了所需的依赖库
- 模型文件应该是ply类型
