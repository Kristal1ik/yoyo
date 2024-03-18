import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from math_model_maxwell import Maths_Model_Maxwell


class PyGameWidget(QtWidgets.QLabel):
    def __init__(self, game=None, timer_delay=5, *args, **kwargs):
        assert game is not None
        super(PyGameWidget, self).__init__(*args, **kwargs)
        self.image = QtGui.QImage()
        self.game = game()
        self.timer = QTimer()
        self.timer.start(timer_delay)
        self.flag = True
        self.timer.timeout.connect(self.pygame_loop)

    def pygame_loop(self):
        surface = self.game.loop()
        w = surface.get_width()
        h = surface.get_height()
        self.data = surface.get_buffer().raw
        self.image = QtGui.QImage(self.data, w, h, QtGui.QImage.Format_RGB32)
        self.setPixmap(QPixmap.fromImage(self.image))
        self.update()


    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PyGameWidget(Maths_Model_Maxwell)
    w.resize(300, 300)
    w.show()
    sys.exit(app.exec_())
