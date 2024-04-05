# main.py
import sys
import numpy as np
import open3d as o3d
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QAction, QFileDialog
from PyQt5.QtOpenGL import QGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *

class OpenGLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(OpenGLWidget, self).__init__(parent)

        self.mesh = None

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("三维模型可视化")
        self.setGeometry(100, 100, 800, 600)

        self.openGLWidget = OpenGLWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.openGLWidget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        import_model_action = QAction("导入模型文件", self)
        import_model_action.triggered.connect(self.import_model)
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("文件")
        file_menu.addAction(import_model_action)

    def import_model(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择模型文件", "", "PLY Files (*.ply)")
        if file_path:
            print("Selected model file:", file_path)
            try:
                # 通过open3d直接读取网格
                self.openGLWidget.mesh = o3d.io.read_triangle_mesh(file_path)
                self.openGLWidget.update()
                # 绘制网格顶点法线
                self.openGLWidget.mesh.compute_vertex_normals()
                o3d.visualization.draw_geometries([self.openGLWidget.mesh])
            except Exception as e:
                print("Error loading model:", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
