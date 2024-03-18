# from PyQt5 import QtCore, QtGui, QtWidgets
# from math_model_maxwell import Maths_Model_Maxwell
# from PyGameWidget import PyGameWidget
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(468, 239)
#         Form.setStyleSheet("background-color: rgb(246, 246, 255);\n"
#                            "")
#         self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
#         self.verticalLayout_5.setObjectName("verticalLayout_5")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout()
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         spacerItem = QtWidgets.QSpacerItem(34, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout.addItem(spacerItem)
#         self.comboBox = QtWidgets.QComboBox(Form)
#         self.comboBox.setStyleSheet("color: rgb(45, 44, 45);\n"
#                                     "font: 300 17px \"Segoe UI\";")
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("Максвелла")
#         self.comboBox.addItem("Перевернутый   ")
#         self.horizontalLayout.addWidget(self.comboBox)
#         self.verticalLayout_4.addLayout(self.horizontalLayout)
#         self.verticalLayout_5.addLayout(self.verticalLayout_4)
#         self.formLayout = QtWidgets.QFormLayout()
#         self.formLayout.setObjectName("formLayout")
#         self.verticalLayout = QtWidgets.QVBoxLayout()
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout()
#         self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.label_2 = QtWidgets.QLabel(Form)
#         self.label_2.setStyleSheet("color: rgb(45, 44, 45);\n"
#                                    "font: 300 14px \"Segoe UI\";")
#         self.label_2.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_2.setObjectName("label_2")
#         self.verticalLayout_2.addWidget(self.label_2)
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.x_label = QtWidgets.QLabel(Form)
#         self.x_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.x_label.setObjectName("x_label")
#         self.horizontalLayout_3.addWidget(self.x_label)
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setObjectName("label")
#         self.horizontalLayout_3.addWidget(self.label)
#         self.verticalLayout_2.addLayout(self.horizontalLayout_3)
#         self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_4.setObjectName("horizontalLayout_4")
#         self.label_3 = QtWidgets.QLabel(Form)
#         self.label_3.setStyleSheet("color: rgb(45, 44, 45);\n"
#                                    "font: 300 14px \"Segoe UI\";")
#         self.label_3.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_3.setObjectName("label_3")
#         self.horizontalLayout_4.addWidget(self.label_3)
#         self.pushButton = QtWidgets.QPushButton(Form)
#         self.pushButton.setObjectName("pushButton")
#         self.horizontalLayout_4.addWidget(self.pushButton)
#         self.verticalLayout_2.addLayout(self.horizontalLayout_4)
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout()
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.label_4 = QtWidgets.QLabel(Form)
#         self.label_4.setStyleSheet("color: rgb(45, 44, 45);\n"
#                                    "font: 300 14px \"Segoe UI\";\n"
#                                    "")
#         self.label_4.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_4.setObjectName("label_4")
#         self.verticalLayout_3.addWidget(self.label_4)
#         self.label_5 = QtWidgets.QLabel(Form)
#         self.label_5.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_5.setObjectName("label_5")
#         self.verticalLayout_3.addWidget(self.label_5)
#         self.verticalLayout_2.addLayout(self.verticalLayout_3)
#         self.verticalLayout.addLayout(self.verticalLayout_2)
#         self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
#
#
#
#         # self.image = QtWidgets.QWidget()
#         # self.image = PyGameWidget(Maths_Model_Maxwell)
#         # self.verticalLayout_5.addWidget(self.image)
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.label_2.setText(_translate("Form", "TextLabel"))
#         self.x_label.setText(_translate("Form", "TextLabel"))
#         self.label.setText(_translate("Form", "TextLabel"))
#         self.label_3.setText(_translate("Form", "TextLabel"))
#         self.pushButton.setText(_translate("Form", "PushButton"))
#         self.label_4.setText(_translate("Form", "TextLabel"))
#         self.label_5.setText(_translate("Form", "TextLabel"))
#
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'math_model_maxwell.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

from math_model_maxwell import Maths_Model_Maxwell
from PyGameWidget import PyGameWidget



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(468, 239)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(34, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("color: rgb(45, 44, 45);\n"
                                   "font: 300 14px \"Segoe UI\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.x_label = QtWidgets.QLabel(Form)
        self.x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.x_label.setObjectName("x_label")
        self.horizontalLayout_3.addWidget(self.x_label)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("color: rgb(45, 44, 45);\n"
                                   "font: 300 14px \"Segoe UI\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("color: rgb(45, 44, 45);\n"
                                   "font: 300 14px \"Segoe UI\";\n"
                                   "")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.img = PyGameWidget(game=Maths_Model_Maxwell)
        self.img.setObjectName("img")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.img)
        self.verticalLayout_5.addLayout(self.formLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.x_label.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "TextLabel"))


class Math_Model_Maxwell_Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
