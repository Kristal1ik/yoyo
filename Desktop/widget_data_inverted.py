from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(691, 375)
        Form.setStyleSheet("background-color: rgb(246, 246, 255);")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 17px \"Segoe UI\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Максвелла")
        self.comboBox.addItem("Перевернутый   ")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(15, 25, 15, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.params_1 = QtWidgets.QFrame(Form)
        self.params_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px; \n"
                                    "")
        self.params_1.setObjectName("params_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.params_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_50 = QtWidgets.QLabel(self.params_1)
        self.label_50.setStyleSheet("color: rgb(0, 0, 255);\n"
                                    "font: 300 24px\"Segoe UI\";\n"
                                    "")
        self.label_50.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_3.addWidget(self.label_50)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_48 = QtWidgets.QLabel(self.params_1)
        self.label_48.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_48.setObjectName("label_48")
        self.verticalLayout.addWidget(self.label_48)
        self.label_51 = QtWidgets.QLabel(self.params_1)
        self.label_51.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_51.setObjectName("label_51")
        self.verticalLayout.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(self.params_1)
        self.label_52.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_52.setObjectName("label_52")
        self.verticalLayout.addWidget(self.label_52)
        self.label_53 = QtWidgets.QLabel(self.params_1)
        self.label_53.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_53.setObjectName("label_53")
        self.verticalLayout.addWidget(self.label_53)
        self.label_54 = QtWidgets.QLabel(self.params_1)
        self.label_54.setStyleSheet("color: rgb(45, 44, 45);color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_54.setObjectName("label_54")
        self.verticalLayout.addWidget(self.label_54)
        self.label_55 = QtWidgets.QLabel(self.params_1)
        self.label_55.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_55.setObjectName("label_55")
        self.verticalLayout.addWidget(self.label_55)
        self.label_56 = QtWidgets.QLabel(self.params_1)
        self.label_56.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_56.setObjectName("label_56")
        self.verticalLayout.addWidget(self.label_56)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.params_1)
        self.lineEdit_47.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.verticalLayout_2.addWidget(self.lineEdit_47)
        self.lineEdit_48 = QtWidgets.QLineEdit(self.params_1)
        self.lineEdit_48.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.verticalLayout_2.addWidget(self.lineEdit_48)
        self.lineEdit_49 = QtWidgets.QLineEdit(self.params_1)
        self.lineEdit_49.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.verticalLayout_2.addWidget(self.lineEdit_49)
        self.lineEdit_50 = QtWidgets.QLineEdit(self.params_1)
        self.lineEdit_50.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.verticalLayout_2.addWidget(self.lineEdit_50)
        self.lineEdit_51 = QtWidgets.QLineEdit(self.params_1)
        self.lineEdit_51.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.verticalLayout_2.addWidget(self.lineEdit_51)
        self.lineEdit_52 = QtWidgets.QLineEdit(self.params_1)
        self.lineEdit_52.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.verticalLayout_2.addWidget(self.lineEdit_52)
        self.lineEdit_53 = QtWidgets.QLineEdit(self.params_1)
        self.lineEdit_53.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.verticalLayout_2.addWidget(self.lineEdit_53)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.params_1)
        self.params_2 = QtWidgets.QFrame(Form)
        self.params_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px; ")
        self.params_2.setObjectName("params_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.params_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_58 = QtWidgets.QLabel(self.params_2)
        self.label_58.setStyleSheet("color: rgb(0, 0, 255);\n"
                                    "font: 300 24px\"Segoe UI\";\n"
                                    "")
        self.label_58.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_4.addWidget(self.label_58)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_49 = QtWidgets.QLabel(self.params_2)
        self.label_49.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_49.setObjectName("label_49")
        self.verticalLayout_5.addWidget(self.label_49)
        self.label_63 = QtWidgets.QLabel(self.params_2)
        self.label_63.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_63.setObjectName("label_63")
        self.verticalLayout_5.addWidget(self.label_63)
        self.label_64 = QtWidgets.QLabel(self.params_2)
        self.label_64.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_64.setObjectName("label_64")
        self.verticalLayout_5.addWidget(self.label_64)
        self.label_65 = QtWidgets.QLabel(self.params_2)
        self.label_65.setStyleSheet("color: rgb(45, 44, 45);\n"
                                    "font: 300 14px \"Segoe UI\";")
        self.label_65.setObjectName("label_65")
        self.verticalLayout_5.addWidget(self.label_65)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.params_2)
        self.lineEdit_55.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.verticalLayout_6.addWidget(self.lineEdit_55)
        self.lineEdit_60 = QtWidgets.QLineEdit(self.params_2)
        self.lineEdit_60.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.verticalLayout_6.addWidget(self.lineEdit_60)
        self.lineEdit_61 = QtWidgets.QLineEdit(self.params_2)
        self.lineEdit_61.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.verticalLayout_6.addWidget(self.lineEdit_61)
        self.lineEdit_62 = QtWidgets.QLineEdit(self.params_2)
        self.lineEdit_62.setStyleSheet("     border-width: 0.5px;\n"
                                       "     border-style: solid;\n"
                                       "     border-radius: 4px;\n"
                                       "border-color: #8f8f8f\n"
                                       "")
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.verticalLayout_6.addWidget(self.lineEdit_62)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.params_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("background-color: blue;\n"
                                      "     border-style: outset;\n"
                                      "     border-radius: 10px;\n"
                                      "     border-color: beige;\n"
                                      "    font: 300 20px \"Segoe UI\";\n"
                                      "color: white;\n"
                                      "     padding: 6px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_50.setText(_translate("Form", "Параметры маятника"))
        self.label_48.setText(_translate("Form", "Длина стержня"))
        self.label_51.setText(_translate("Form", "Масса тележки"))
        self.label_52.setText(_translate("Form", "Масса груза"))
        self.label_53.setText(_translate("Form", "Шаг измерений"))
        self.label_54.setText(_translate("Form", "Время измерений"))
        self.label_55.setText(_translate("Form", "Начальная координата"))
        self.label_56.setText(_translate("Form", "Начальная скорость"))
        self.label_58.setText(_translate("Form", "Параметры ген.алгоритма"))
        self.label_49.setText(_translate("Form", "Количество особей"))
        self.label_63.setText(_translate("Form", "Количество поколений"))
        self.label_64.setText(_translate("Form", "Верхняя граница желаемой траектории"))
        self.label_65.setText(_translate("Form", "Нижняя граница желаемой траектории"))
        self.pushButton.setText(_translate("Form", "Сохранить"))


class Data_Widget_Inverted(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
