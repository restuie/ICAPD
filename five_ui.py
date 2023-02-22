# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'five.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(145, 140, 970, 800))
        self.label.setStyleSheet("box-sizing: border-box;\n"
"position: absolute;\n"
"border: 10px solid #00BDC9;\n"
"border-radius: 60px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 64px;\n"
"line-height: 77px;\n"
"color: #00BDC9;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1200, 140, 577, 479))
        self.frame.setStyleSheet("box-sizing: border-box;\n"
"position: absolute;\n"
"border: 10px solid #00BDC9;\n"
"border-radius: 60px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 401, 151))
        self.label_2.setStyleSheet("font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 100px;\n"
"line-height: 121px;\n"
"border-radius: 0px;\n"
"border: 0px solid #ffffff;\n"
"color: #00BDC9;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(180, 220, 211, 151))
        self.label_3.setStyleSheet("font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 100px;\n"
"line-height: 121px;\n"
"border-radius: 0px;\n"
"border: 0px solid #ffffff;\n"
"color: #00BDC9;\n"
"")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1244, 722, 200, 200))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-image:url(img/5-1.png);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    margin: 10px;\n"
"}\n"
" ")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1530, 720, 200, 200))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border-image:url(img/5-2.png);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    margin: 10px;\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "照片"))
        self.label_2.setText(_translate("MainWindow", "辨識結果"))
        self.label_3.setText(_translate("MainWindow", "清澈"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

