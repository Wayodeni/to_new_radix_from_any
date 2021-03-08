# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scales_of_notation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(267, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputNum = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNum.setEnabled(True)
        self.inputNum.setInputMask("")
        self.inputNum.setObjectName("inputNum")
        self.verticalLayout.addWidget(self.inputNum)
        self.numRadix = QtWidgets.QLineEdit(self.centralwidget)
        self.numRadix.setObjectName("numRadix")
        self.verticalLayout.addWidget(self.numRadix)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.outputRadix = QtWidgets.QLineEdit(self.centralwidget)
        self.outputRadix.setObjectName("outputRadix")
        self.verticalLayout.addWidget(self.outputRadix)
        self.getResult = QtWidgets.QPushButton(self.centralwidget)
        self.getResult.setObjectName("getResult")
        self.verticalLayout.addWidget(self.getResult)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.outputNum = QtWidgets.QLineEdit(self.centralwidget)
        self.outputNum.setAlignment(QtCore.Qt.AlignCenter)
        self.outputNum.setObjectName("outputNum")
        self.verticalLayout.addWidget(self.outputNum)
        self.errorOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.errorOutput.setEnabled(True)
        self.errorOutput.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorOutput.setReadOnly(True)
        self.errorOutput.setCenterOnScroll(False)
        self.errorOutput.setObjectName("errorOutput")
        self.verticalLayout.addWidget(self.errorOutput)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Перевод систем счисления"))
        self.inputNum.setText(_translate("MainWindow", "Начальное число"))
        self.inputNum.setPlaceholderText(_translate("MainWindow", "Начальное число"))
        self.numRadix.setText(_translate("MainWindow", "Основание системы счисления"))
        self.numRadix.setPlaceholderText(_translate("MainWindow", "Основание системы счисления"))
        self.outputRadix.setText(_translate("MainWindow", "Система счисления конечного числа"))
        self.outputRadix.setPlaceholderText(_translate("MainWindow", "Система счисления конечного числа"))
        self.getResult.setText(_translate("MainWindow", "Перевести"))
        self.outputNum.setText(_translate("MainWindow", "Результат"))
        self.outputNum.setPlaceholderText(_translate("MainWindow", "Результат"))
        self.errorOutput.setPlaceholderText(_translate("MainWindow", "Ошибки, допущенные при вводе."))
