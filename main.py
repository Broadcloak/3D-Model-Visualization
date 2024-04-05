# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QAction, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtOpenGL import QGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtCore import Qt, QPoint
import pywavefront

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

class ModelVisualization(QGLWidget):
    def __init__(self, parent=None):
        super(ModelVisualization, self).__init__(parent)

        self.rotate_x = 0
        self.rotate_y = 0
        self.last_pos = QPoint()

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -5.0)  # 调整模型位置
        glRotatef(self.rotate_x, 1, 0, 0)  # 绕x轴旋转
        glRotatef(self.rotate_y, 0, 1, 0)  # 绕y轴旋转

        glBegin(GL_QUADS)
        for surface in surfaces:
            for vertex_i in surface:
                glVertex3fv(vertices[vertex_i])
        glEnd()

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.last_pos.x()
        dy = event.y() - self.last_pos.y()

        self.rotate_x += dy
        self.rotate_y += dx

        self.last_pos = event.pos()
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("三维模型可视化窗口")
        self.setGeometry(900, 400, 800, 600)

        cube_visualization = ModelVisualization(self)

        layout = QVBoxLayout()
        layout.addWidget(cube_visualization)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        import_model_action = QAction("导入模型文件", self)
        import_model_action.triggered.connect(self.import_model)
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("文件")
        file_menu.addAction(import_model_action)

    def import_model(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择模型文件", "", "Model Files (*.obj *.h5 *.pb)")
        if file_path:
            print("选择模型文件:", file_path)
            model = pywavefront.Wavefront(file_path)
            if model:
                if self.model_visualization:
                    self.layout().removeWidget(self.model_visualization)
                    self.model_visualization.deleteLater()
                self.model_visualization = ModelVisualization(model, self)
                self.layout().addWidget(self.model_visualization)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
