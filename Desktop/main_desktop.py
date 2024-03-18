import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCheckBox, QBoxLayout, QVBoxLayout, QWidget, \
    QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from PyQt5 import QtCore, QtGui, QtWidgets

from Desktop.base_widget import Base_Widget
from sidebar_ui import Ui_MainWindow
from widget_data_inverted import Data_Widget_Inverted
from widget_data import Data_Widget
from math_model_maxwell_widget import Math_Model_Maxwell_Widget
from graph_maxwell import Graph_Maxwell
from global_vars import Global_Vars


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.comboBox_state = "Максвелла"
        self.data_maxwell = False
        self.pg_max_count = False
        self.graph_maxwell_count = False
        self.base_maxwell = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)

        self.widget_data_inverted = Data_Widget_Inverted()
        self.widget_data_inverted.setObjectName("widget_data_inverted")

        self.widget_data = Data_Widget()
        self.widget_data.setObjectName("widget_data")
        self.ui.gridLayout_2.addWidget(self.widget_data)

        self.widget_base = Base_Widget()
        self.widget_base.setObjectName("widget_base")
        self.widget_base_inverted = Base_Widget()
        self.widget_base_inverted.setObjectName("widget_base_inverted")
        self.widget_base_inverted.pushButton_3.clicked.connect(self.click_open_base_inv)
        self.widget_base_inverted.pushButton_2.clicked.connect(self.click_save_base_maxwell)

        self.ui.home_btn_2.setChecked(True)

        self.x = []
        self.v = []
        self.w = []

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
        try:
            Global_Vars.m = float(self.widget_data.lineEdit_47.text())
            Global_Vars.maxis = float(self.widget_data.lineEdit_48.text())
            Global_Vars.r = float(self.widget_data.lineEdit_49.text())
            Global_Vars.dt = float(self.widget_data.lineEdit_50.text())
            Global_Vars.T = int(self.widget_data.lineEdit_51.text())
            Global_Vars.x0 = float(self.widget_data.lineEdit_52.text())
            Global_Vars.v0 = float(self.widget_data.lineEdit_53.text())
            Global_Vars.l = float(self.widget_data.lineEdit_54.text())
            Global_Vars.x1 = float(self.widget_data.lineEdit_61.text())
            Global_Vars.x2 = float(self.widget_data.lineEdit_62.text())
            if Global_Vars.l < Global_Vars.x2 + 0.05:
                raise ValueError
            elif Global_Vars.x1 > Global_Vars.x2:
                raise Warning

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Данные сохранены!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
            return

        except Warning:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Некорректные данные:\nНижняя граница должна быть больше вкрхней границы!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Некорректные данные:\nНижняя граница должна быть меньше длины пути!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
            return
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Некорректные данные!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
            return

    def click_data_inverted(self):
        print("inv")
        try:
            Global_Vars.L_inv = float(self.widget_data.lineEdit_47.text())
            Global_Vars.m_inv = float(self.widget_data.lineEdit_48.text())
            Global_Vars.M_inv = float(self.widget_data.lineEdit_49.text())
            Global_Vars.dt_inv = float(self.widget_data.lineEdit_50.text())
            Global_Vars.T_inv = float(self.widget_data.lineEdit_51.text())
            Global_Vars.x0_inv = float(self.widget_data.lineEdit_52.text())
            Global_Vars.v0_inv = float(self.widget_data.lineEdit_53.text())
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Данные сохранены!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Некорректные данные!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
            return

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
        else:
            self.widget_data.comboBox.setCurrentText("Максвелла")
            self.widget_data_inverted.comboBox.setCurrentText("Перевернутый   ")
            self.widget_data.comboBox.activated.connect(self.onActivated)
            self.ui.gridLayout_2.replaceWidget(self.widget_data_inverted, self.widget_data)
            self.widget_data_inverted.close()
            self.widget_data_inverted = Data_Widget_Inverted()
            self.widget_data_inverted.setObjectName("widget_data_inverted")

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        if not self.pg_max_count:
            self.pg_max_count = True
            self.pg_widget_maxwell = Math_Model_Maxwell_Widget()
            self.ui.gridLayout_3.addWidget(self.pg_widget_maxwell)

    def click_open_base_maxwell(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt)")
        try:
            if filename:
                with open(filename, encoding='utf8') as f:

                    text_file = []
                    for line in f.readlines():
                        text_file.extend(list(map(float, line.split(", "))))
                    print(text_file)
                    n = 0
                    for i in range(5):
                        for j in range(12):
                            print(text_file[n])
                            self.widget_base.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(text_file[n])))
                            n += 1
                            self.widget_base.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Файл не выбран!")
                msg.setWindowTitle("Уведомление")
                msg.exec_()
                return
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Некорректные данные!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
            return
    def click_save_base_maxwell(self):
        filename, ok = QFileDialog.getSaveFileName(self,
                                                   "Сохранить файл",
                                                   ".",
                                                   "Text Files(*.txt)")
        if filename:
            with open(filename, "w") as file:
                for i in range(self.widget_base.tableWidget.rowCount()):
                    for j in range(self.widget_base.tableWidget.columnCount()):
                        if j == self.widget_base.tableWidget.columnCount() - 1:
                            file.write(self.widget_base.tableWidget.item(i, j).text())
                        else:
                            file.write(self.widget_base.tableWidget.item(i, j).text() + ", ")
                    file.write("\n")
                file.close()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Файл <br><b>{}</b> <br> успешно сохранён!".format(filename.split('/')[-1]))
            msg.setWindowTitle("Уведомление")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Имя файла не указано!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
            return

    def click_open_base_inv(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt)")
        try:
            if filename:
                with open(filename, encoding='utf8') as f:

                    text_file = []
                    for line in f.readlines():
                        text_file.extend(list(map(float, line.split(", "))))
                    print(text_file)
                    n = 0
                    for i in range(5):
                        for j in range(12):
                            print(text_file[n])
                            self.widget_base_inverted.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(text_file[n])))
                            n += 1
                            self.widget_base_inverted.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Файл не выбран!")
                msg.setWindowTitle("Уведомление")
                msg.exec_()
                return
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Некорректные данные!")
            msg.setWindowTitle("Уведомление")
            msg.exec_()
            return
    def on_orders_btn_2_toggled(self):
        if not self.base_maxwell:
            self.ui.gridLayout_4.addWidget(self.widget_base)
            self.base_maxwell = True
        self.widget_base.pushButton_3.clicked.connect(self.click_open_base_maxwell)
        self.widget_base.pushButton_2.clicked.connect(self.click_save_base_maxwell)
        self.widget_base.comboBox.activated.connect(self.onActivated3)
        self.ui.stackedWidget.setCurrentIndex(2)

    def onActivated3(self):
        text = self.widget_base.comboBox.currentText().strip()
        print(self.widget_base.comboBox)
        print(text)
        print(self.widget_base.comboBox.currentText())
        if text == "Перевернутый":
            self.widget_base_inverted.comboBox.setCurrentText("Перевернутый   ")
            self.widget_base.comboBox.setCurrentText("Максвелла")
            self.widget_base_inverted.comboBox.activated.connect(self.onActivated3)
            self.ui.gridLayout_4.replaceWidget(self.widget_base, self.widget_base_inverted)
            self.widget_base.close()
            self.widget_base = Base_Widget()
            self.widget_base.setObjectName("widget_base")
            self.widget_base.pushButton_3.clicked.connect(self.click_open_base_maxwell)
            self.widget_base.pushButton_2.clicked.connect(self.click_save_base_maxwell)
        else:
            self.widget_base.comboBox.setCurrentText("Максвелла")
            self.widget_base_inverted.comboBox.setCurrentText("Перевернутый   ")
            self.widget_base.comboBox.activated.connect(self.onActivated3)
            self.ui.gridLayout_4.replaceWidget(self.widget_base_inverted, self.widget_base)
            self.widget_base_inverted.close()
            self.widget_base_inverted = Base_Widget()
            self.widget_base_inverted.setObjectName("widget_base_inverted")
            self.widget_base_inverted.pushButton_3.clicked.connect(self.click_open_base_maxwell)
            self.widget_base_inverted.pushButton_2.clicked.connect(self.click_save_base_inv)

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
