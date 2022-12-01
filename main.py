import random
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5 import uic


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False

        self.pushButton.clicked.connect(self.on_button_click)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        if self.do_paint == True:
            self.draw_ellipse(qp)
        self.do_paint = False
        qp.end()

    def on_button_click(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp: QPainter):
        qp.setBrush(self.make_brush())
        size = random.randint(0, 500)

        qp.drawEllipse(
            (500 - size) / 2,
            (500 - size) / 2 + 50,
            size,
            size
        )

    def make_brush(self):
        return QBrush(QColor(255, 255, 0))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
