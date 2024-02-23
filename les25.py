from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QInputDialog, QColorDialog
from PyQt6.QtGui import QPixmap, QPainter, QPen, QAction, QColor, QBrush
from PyQt6.QtCore import Qt, QPoint, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Best Paint Application")
        self.setGeometry(100,100,600,400)

        self.label = QLabel(self)
        self.canvas = QPixmap(self.size())
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.last_point = QPoint()
        self.drawing = False


        self.brush_size = 3
        self.brush_color = Qt.GlobalColor.black
        self.current_tool = 'pen'
        self.initUI()

    def initUI(self):
        self.toolBar = QToolBar('Инструменты')
        self.addToolBar(self.toolBar)

        penAction = QAction('Pen', self)
        penAction.triggered.connect(self.selectPen)
        self.toolBar.addAction(penAction)

        brushAction = QAction('Brush', self)
        brushAction.triggered.connect(self.selectBrush)
        self.toolBar.addAction(brushAction)


        colorAction = QAction('Color', self)
        colorAction.triggered.connect(self.selectColor)
        self.toolBar.addAction(colorAction)

    def selectColor(self):
        color = QColorDialog.getColor(self.brush_color, self)
        if color.isValid():
            self.brush_color = color

    def selectBrush(self):
        size, succes = QInputDialog.getInt(self, 'Size Brush', 'Select Brush',min=1, max=20)
        if succes:
            self.brush_size =size
    def selectPen(self):
        self.current_tool = 'pen'

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self.drawing == True:
            pm = self.label.pixmap()
            painter = QPainter(pm)
            pen = QPen(self.brush_color, self.brush_size, Qt.PenStyle.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.position().toPoint())
            painter.end()
            self.label.setPixmap(pm)
            # self.last_point = event.position.toPoint()
            # self.label.update()


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Вы отпустили ЛКМ")
            self.drawing=False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



