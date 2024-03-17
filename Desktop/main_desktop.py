import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCheckBox, QBoxLayout, QVBoxLayout, QWidget, \
    QMessageBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from sidebar_ui import Ui_MainWindow
from widget_data_inverted import Data_Widget_Inverted
from widget_data import Data_Widget
from math_model_maxwell_widget import Math_Model_Maxwell_Widget
from graph_maxwell import Graph_Maxwell


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.comboBox_state = "Максвелла"
        self.data_maxwell = False
        self.pg_max_count = False
        self.graph_maxwell_count = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)

        self.widget_data_inverted = Data_Widget_Inverted()
        self.widget_data_inverted.setObjectName("widget_data_inverted")
        self.widget_data = Data_Widget()
        self.widget_data.setObjectName("widget_data")
        self.ui.gridLayout_2.addWidget(self.widget_data)
        self.ui.home_btn_2.setChecked(True)

        self.x = []
        self.v = []
        self.w = []
        self.m = 0.5  # масса диска
        self.g = 9.8
        self.maxis = 0.01  # масса оси
        self.r = 0.002  # радиус диска !
        self.R = 0.03  # радиус оси
        self.dt = 0.01  # шаг измерений
        self.T = 60  # времня измерений
        self.x0 = 0.05  # начальная координата
        self.v0 = 0  # начальная скорость
        self.l = 0.5  # длина пути
        # F1 = -20
        # F2 = 20
        # k = 0.1
        # e = 0.000001

        self.L = 1.0  # длина стержня
        self.m = 0.5
        M = 1.0

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
        # self.ui.gridLayout_2.addWidget(self.widget_data)
        # print("fghj")
        self.widget_data.comboBox.activated.connect(self.onActivated)
        self.widget_data.pushButton.clicked.connect(self.click_data_maxwell)
        self.widget_data_inverted.pushButton.clicked.connect(self.click_data_inverted)
        # print(self.widget_data.comboBox)

    def click_data_maxwell(self):
        print("max")

    def click_data_inverted(self):
        print("inv")

    def onActivated(self):
        text = self.widget_data.comboBox.currentText().strip()
        print(self.widget_data.comboBox)
        print(text)
        print(self.widget_data.comboBox.currentText())
        if text == "Перевернутый":
            self.widget_data_inverted.comboBox.setCurrentText("Перевернутый   ")
            self.widget_data.comboBox.setCurrentText("Максвелла")
            self.widget_data_inverted.comboBox.activated.connect(self.onActivated)
            self.ui.gridLayout_2.replaceWidget(self.widget_data, self.widget_data_inverted)
            self.widget_data.close()
            self.widget_data = Data_Widget()
            self.widget_data.setObjectName("widget_data")
            # del self.widget_data
        else:
            self.widget_data.comboBox.setCurrentText("Максвелла")
            self.widget_data_inverted.comboBox.setCurrentText("Перевернутый   ")
            self.widget_data.comboBox.activated.connect(self.onActivated)
            # self.widget_data.comboBox.setCurrentText("Перевернутый   ")
            self.ui.gridLayout_2.replaceWidget(self.widget_data_inverted, self.widget_data)
            self.widget_data_inverted.close()
            self.widget_data_inverted = Data_Widget_Inverted()
            self.widget_data_inverted.setObjectName("widget_data_inverted")
            # del self.widget_data_inverted

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        if not self.pg_max_count:
            self.pg_max_count = True
            # self.pg_widget_maxwell = PyGameWidget(Maths_Model_Maxwell)
            self.pg_widget_maxwell = Math_Model_Maxwell_Widget()
            self.ui.gridLayout_3.addWidget(self.pg_widget_maxwell)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        if not self.graph_maxwell_count:
            self.graph_maxwell_count = True
            self.graph_maxwell = Graph_Maxwell()
        self.ui.gridLayout_5.addWidget(self.graph_maxwell)


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
