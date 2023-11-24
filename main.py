import sys
import random
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.buton = ''
        self.x = 0
        self.y = 0
        self.size = 0
        self.color = QColor(255, 219, 139)
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Супрематизм')
        self.do_paint = False
        self.btn = QPushButton('кнопка', self)
        self.btn.setGeometry(140, 50, 60, 20)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(self.color)
            self.draw(qp)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        for i in range(10):
            self.size = random.randint(20, 201)
            self.x = random.randint(0, 601)
            self.y = random.randint(0, 601)
            qp.drawEllipse(int(self.x - self.size / 2), int(self.y - self.size / 2), self.size, self.size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())