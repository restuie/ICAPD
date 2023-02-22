# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eecs/ICAPD/three.ui'
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
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setEnabled(True)
        self.frame_5.setGeometry(QtCore.QRect(20, 20, 1800, 960))
        self.frame_5.setStyleSheet("background: rgba(255, 255, 255, 0.7);\n"
"border: 10px solid #85D2CF;\n"
"border-radius: 60px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label11 = QtWidgets.QLabel(self.frame_5)
        self.label11.setGeometry(QtCore.QRect(590, 260, 700, 341))
        self.label11.setStyleSheet("border: 0px solid #ffffff;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 120px;\n"
"border-radius: 0px;\n"
"color: #00BDC9;\n"
"background: rgba(255, 255, 255, 0);")
        self.label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label11.setObjectName("label11")
        self.Finish_btn_2 = QtWidgets.QPushButton(self.frame_5)
        self.Finish_btn_2.setGeometry(QtCore.QRect(450, 700, 1010, 200))
        self.Finish_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Finish_btn_2.setStyleSheet("\n"
"QPushButton {\n"
"    border-image:url(img/3-5.png);\n"
"    border-bottom:0px solid #FFFFFF;\n"
"    border-left:0px solid #FFFFFF;\n"
"    border-right:0px solid #FFFFFF;\n"
"    border-top:0px solid #FFFFFF;\n"
"    border-radius: 0px;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    margin:10px;\n"
"}\n"
"")
        self.Finish_btn_2.setText("")
        self.Finish_btn_2.setObjectName("Finish_btn_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setGeometry(QtCore.QRect(70, 70, 168, 198))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("\n"
"QPushButton {\n"
"    border-image:url(img/3-6.png);\n"
"    border-bottom:0px solid #FFFFFF;\n"
"    border-left:0px solid #FFFFFF;\n"
"    border-right:0px solid #FFFFFF;\n"
"    border-top:0px solid #FFFFFF;\n"
"    border-radius: 0px;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    margin:10px;\n"
"}\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(-1, -1, 1921, 1011))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame = QtWidgets.QFrame(self.frame_6)
        self.frame.setGeometry(QtCore.QRect(150, 130, 770, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("border: 10px solid #FF5555;\n"
"border-radius: 60px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setGeometry(QtCore.QRect(50, 50, 120, 120))
        self.label_1.setStyleSheet("border: 0px solid;\n"
"border-image:url(img/3-2.png);\n"
"border-radius: 0px;\n"
"\n"
"")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 420, 110))
        self.label_2.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 100px;\n"
"line-height: 77px;\n"
"color: #FFFFFF;")
        self.label_2.setObjectName("label_2")
        self.label_Show_Temp_2 = QtWidgets.QLabel(self.frame)
        self.label_Show_Temp_2.setGeometry(QtCore.QRect(0, 200, 530, 200))
        self.label_Show_Temp_2.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 150px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #FFFFFF;")
        self.label_Show_Temp_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Show_Temp_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Show_Temp_2.setObjectName("label_Show_Temp_2")
        self.heating_scroll = QtWidgets.QLabel(self.frame)
        self.heating_scroll.setGeometry(QtCore.QRect(0, 480, 770, 220))
        self.heating_scroll.setStyleSheet("border-radius: 60px;\n"
"background: #FF5555;\n"
"border-bottom:0px solid #FF5555;\n"
"border-left:0px solid #FF5555;\n"
"border-right:0px solid #FF5555;\n"
"border-top:0px solid #FF5555;\n"
"color:#FFFFFF;\n"
"")
        self.heating_scroll.setText("")
        self.heating_scroll.setObjectName("heating_scroll")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(620, 270, 101, 101))
        self.label_4.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 100px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #FFFFFF;")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.stopheating = QtWidgets.QPushButton(self.frame)
        self.stopheating.setGeometry(QtCore.QRect(50, 520, 680, 150))
        self.stopheating.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopheating.setStyleSheet("\n"
"QPushButton {\n"
"    border-radius: 60px;\n"
"    background: #FFFFFF;\n"
"    border:10px solid #E30505;\n"
"    border-radius: 60px;\n"
"    color: #E30505;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 80px;\n"
"}\n"
"QPushButton:hover {\n"
"    margin:10px;\n"
"}\n"
" \n"
"\n"
"")
        self.stopheating.setObjectName("stopheating")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 790, 481))
        self.frame_2.setStyleSheet("border-bottom: 0px solid #FFFFFF;\n"
"border-left: 0px solid #FFFFFF;\n"
"border-right: 0px solid #FFFFFF;\n"
"border-top: 0px solid #FFFFFF;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_1_1 = QtWidgets.QLabel(self.frame_2)
        self.label_1_1.setGeometry(QtCore.QRect(50, 50, 120, 120))
        self.label_1_1.setStyleSheet("border: 0px solid;\n"
"border-image:url(img/3-1.png);\n"
"border-radius: 0px;\n"
"\n"
"")
        self.label_1_1.setText("")
        self.label_1_1.setObjectName("label_1_1")
        self.label_2_1 = QtWidgets.QLabel(self.frame_2)
        self.label_2_1.setGeometry(QtCore.QRect(200, 50, 420, 110))
        self.label_2_1.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 100px;\n"
"line-height: 77px;\n"
"color: #FF5555;")
        self.label_2_1.setObjectName("label_2_1")
        self.label_Show_Temp = QtWidgets.QLabel(self.frame_2)
        self.label_Show_Temp.setGeometry(QtCore.QRect(0, 200, 530, 200))
        self.label_Show_Temp.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 150px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #FF5555;")
        self.label_Show_Temp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Show_Temp.setObjectName("label_Show_Temp")
        self.label_4_1 = QtWidgets.QLabel(self.frame_2)
        self.label_4_1.setGeometry(QtCore.QRect(620, 270, 101, 101))
        self.label_4_1.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 100px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #FF5555;")
        self.label_4_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4_1.setObjectName("label_4_1")
        self.heating_scroll.raise_()
        self.label_1.raise_()
        self.label_2.raise_()
        self.label_Show_Temp_2.raise_()
        self.label_4.raise_()
        self.stopheating.raise_()
        self.frame_2.raise_()
        self.frame_3 = QtWidgets.QFrame(self.frame_6)
        self.frame_3.setGeometry(QtCore.QRect(1000, 130, 770, 700))
        self.frame_3.setStyleSheet("border: 10px solid #00BDC9;\n"
"border-radius: 60px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(-1, -1, 770, 220))
        self.frame_4.setStyleSheet("background: #00BDC9;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label5 = QtWidgets.QLabel(self.frame_4)
        self.label5.setGeometry(QtCore.QRect(50, 50, 120, 120))
        self.label5.setStyleSheet("border-image:url(img/3-3.png);\n"
"border-radius: 0px;")
        self.label5.setText("")
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(self.frame_4)
        self.label6.setGeometry(QtCore.QRect(180, 50, 401, 121))
        self.label6.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 100px;\n"
"line-height: 77px;\n"
"color: #FFFFFF;")
        self.label6.setObjectName("label6")
        self.label_Show_Injection_2 = QtWidgets.QLabel(self.frame_4)
        self.label_Show_Injection_2.setGeometry(QtCore.QRect(120, 220, 530, 200))
        self.label_Show_Injection_2.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 200px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #FFFFFF;")
        self.label_Show_Injection_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Show_Injection_2.setObjectName("label_Show_Injection_2")
        self.label8 = QtWidgets.QLabel(self.frame_4)
        self.label8.setGeometry(QtCore.QRect(270, 470, 450, 200))
        self.label8.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 128px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #FFFFFF;")
        self.label8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label8.setObjectName("label8")
        self.label10 = QtWidgets.QLabel(self.frame_3)
        self.label10.setGeometry(QtCore.QRect(270, 470, 450, 200))
        self.label10.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 128px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #00BDC9;")
        self.label10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label10.setObjectName("label10")
        self.label_Show_Injection = QtWidgets.QLabel(self.frame_3)
        self.label_Show_Injection.setGeometry(QtCore.QRect(119, 220, 530, 200))
        self.label_Show_Injection.setStyleSheet("border: 0px solid;\n"
"border-radius: 0px;\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 200px;\n"
"line-height: 182px;\n"
"text-align: center;\n"
"color: #00BDC9;")
        self.label_Show_Injection.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Show_Injection.setObjectName("label_Show_Injection")
        self.label10.raise_()
        self.label_Show_Injection.raise_()
        self.frame_4.raise_()
        self.Finish_btn = QtWidgets.QPushButton(self.frame_6)
        self.Finish_btn.setGeometry(QtCore.QRect(560, 850, 800, 140))
        self.Finish_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Finish_btn.setStyleSheet("\n"
"QPushButton {\n"
"    border-image:url(img/3-4.png);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    margin:10px;\n"
"}\n"
"")
        self.Finish_btn.setText("")
        self.Finish_btn.setObjectName("Finish_btn")
        self.frame_6.raise_()
        self.frame_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label11.setText(_translate("MainWindow", "<html><head/><body><p>換液完成</p><p>請分離管組</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "加溫中..."))
        self.label_Show_Temp_2.setText(_translate("MainWindow", "33.5"))
        self.label_4.setText(_translate("MainWindow", "℃"))
        self.stopheating.setText(_translate("MainWindow", "緊急停止加熱"))
        self.label_2_1.setText(_translate("MainWindow", "加溫中..."))
        self.label_Show_Temp.setText(_translate("MainWindow", "33.5"))
        self.label_4_1.setText(_translate("MainWindow", "℃"))
        self.label6.setText(_translate("MainWindow", "已注入量"))
        self.label_Show_Injection_2.setText(_translate("MainWindow", "0"))
        self.label8.setText(_translate("MainWindow", "毫升"))
        self.label10.setText(_translate("MainWindow", "毫升"))
        self.label_Show_Injection.setText(_translate("MainWindow", "0"))

