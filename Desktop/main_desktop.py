import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCheckBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from sidebar_ui import Ui_MainWindow
from widget_data_inverted import Data_Widget_Inverted
from widget_data import Data_Widget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.comboBox_state = "Максвелла"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        self.widget_data_inverted = Data_Widget_Inverted()
        self.widget_data_inverted.setObjectName("widget_data_inverted")
        self.widget_data_maxwell = Data_Widget()
        self.widget_data_maxwell.setObjectName("widget_data_maxwell")

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
        text = self.ui.widget_data.comboBox.currentText().strip()
        print(self.ui.widget_data.comboBox)
        print(text)
        print(self.ui.widget_data.comboBox.currentText())
        if text == "Перевернутый":
            # self.widget_data_inverted = Data_Widget_Inverted()
            # self.widget_data_inverted.setObjectName("widget_data_inverted")
            # self.widget_data_inverted.comboBox.setCurrentText(text)
            self.widget_data_inverted.comboBox.setCurrentText("Перевернутый   ")
            self.ui.widget_data.comboBox.setCurrentText("Максвелла")
            self.widget_data_inverted.comboBox.activated.connect(self.onActivated)
            self.ui.gridLayout_2.replaceWidget(self.ui.widget_data, self.widget_data_inverted)
        else:
            self.widget_data_maxwell.comboBox.setCurrentText("Максвелла")
            self.widget_data_maxwell.comboBox.activated.connect(self.onActivated)
            self.ui.widget_data.comboBox.setCurrentText("Перевернутый   ")

            self.ui.gridLayout_2.replaceWidget(self.widget_data_inverted, self.widget_data_maxwell)

            # self.widget_data = Data_Widget_Inverted()
            # self.widget_datasetObjectName("widget_data")
            # self.widget_data.comboBox.setCurrentText(text)
            # self.ui.gridLayout_2.replaceWidget(self.ui.widget_data, self.widget_data_inverted)

        # self.ui.widget_data.comboBox.setCurrentText(text)
        # if self.n % 2 == 0:
        #     self.widget_data_inverted = Data_Widget_Inverted()
        #     self.widget_data_inverted.setObjectName("widget_data_inverted")
        #     self.ui.gridLayout_2.replaceWidget(self.ui.widget_data, self.widget_data_inverted)
        # else:
        #     self.widget_data = Data_Widget()
        #     self.widget_data.setObjectName("widget_data")
        #     self.ui.gridLayout_2.replaceWidget(self.widget_data_inverted, self.ui.widget_data)
        # self.n += 1
        # if text == "Максвелла":
        #     self.comboBox_state = "Максвелла"
        #     self.widget_data = Data_Widget()
        #     self.widget_data.setObjectName("widget_data")
        #     self.ui.gridLayout_2.replaceWidget(self.widget_data_inverted, self.ui.widget_data)
        # elif text == "Перевернутый":
        #     self.comboBox_state = "Перевернутый"
        #     self.widget_data_inverted = Data_Widget_Inverted()
        #     self.widget_data_inverted.setObjectName("widget_data_inverted")
        #     self.ui.gridLayout_2.replaceWidget(self.ui.widget_data, self.widget_data_inverted)
        # print(text)

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
