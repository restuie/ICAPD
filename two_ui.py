# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1124, 93, 707, 411))
        self.widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget.setStyleSheet("border-bottom:10px solid #00BDC9;\n"
"border-left:10px solid #00BDC9;\n"
"border-right:10px solid #00BDC9;\n"
"border-top:10px solid #00BDC9;\n"
"border-radius: 60px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(50, 15, 40, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("border: 0px solid #ffffff;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 64px;\n"
"line-height: 77px;\n"
"color: #00BDC9;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("border: 0px solid #ffffff;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 150px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #00BDC9;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("border: 0px solid #ffffff;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 64px;\n"
"line-height: 77px;\n"
"color: #00BDC9;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(1130, 530, 707, 411))
        self.widget_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget_2.setStyleSheet("background: #00BDC9;\n"
"border-radius: 60px;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(50, 12, 40, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setStyleSheet("border: 0px solid #ffffff;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 64px;\n"
"line-height: 77px;\n"
"color: #FFFFFF;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_Show_Injection = QtWidgets.QLabel(self.widget_2)
        self.label_Show_Injection.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_Show_Injection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Show_Injection.setStyleSheet("border: 0px solid #96D8D6;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 150px;\n"
"border-bottom: 5px solid #ffffff;\n"
"border-radius: 0px;\n"
"color: #FFFFFF;")
        self.label_Show_Injection.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Show_Injection.setObjectName("label_Show_Injection")
        self.verticalLayout_3.addWidget(self.label_Show_Injection)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setStyleSheet("border: 0px solid #ffffff;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 64px;\n"
"line-height: 77px;\n"
"\n"
"border-radius: 0px;\n"
"color: #FFFFFF;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.heating_btn = QtWidgets.QPushButton(self.centralwidget)
        self.heating_btn.setGeometry(QtCore.QRect(90, 80, 974, 893))
        self.heating_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.heating_btn.setStyleSheet("QPushButton {\n"
"    border-image:url(img/heating_btn.png);\n"
"}\n"
"QPushButton:hover {\n"
"    margin: 10px;\n"
"}")
        self.heating_btn.setText("")
        self.heating_btn.setObjectName("heating_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "即時重量"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "公克"))
        self.label_4.setText(_translate("MainWindow", "注入量"))
        self.label_Show_Injection.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "毫升"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

