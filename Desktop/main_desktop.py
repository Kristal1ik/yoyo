import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCheckBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from sidebar_ui import Ui_MainWindow

comboBox_state = "Максвелла"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)


    def on_stackedWidget_currentChanged(self, index):

        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                   + self.ui.full_menu_widget.findChildren(QPushButton)
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.widget_data.comboBox.activated.connect(self.onActivated)
        print(self.ui.widget_data.comboBox)
        # self.ui.stackedWidget.addWidget(QPushButton)
    def onActivated(self):
        text = self.ui.widget_data.comboBox.currentText()
        print(text)
    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    style_file = QFile("static/style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    print("fgyhuj")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
