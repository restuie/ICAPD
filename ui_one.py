# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eecs/ICAPD/one.ui'
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
        self.goNextPage = QtWidgets.QPushButton(self.centralwidget)
        self.goNextPage.setGeometry(QtCore.QRect(751, 858, 351, 135))
        self.goNextPage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goNextPage.setStyleSheet("QPushButton {\n"
"    border-radius: 60px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 65px;\n"
"    line-height: 121px;\n"
"    color: #FFFFFF;\n"
"    background: #85D2CF;\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" \n"
"")
        self.goNextPage.setObjectName("goNextPage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(119, 261, 983, 569))
        self.label.setStyleSheet("border: 10px solid #85D2CF;\n"
"border-radius: 65px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(844, 683, 219, 101))
        self.label_2.setStyleSheet("font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 90px;\n"
"line-height: 109px;\n"
"color: #96D8D6;")
        self.label_2.setObjectName("label_2")
        self.show_text = QtWidgets.QLabel(self.centralwidget)
        self.show_text.setGeometry(QtCore.QRect(198, 332, 793, 332))
        self.show_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_text.setStyleSheet("font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 300px;\n"
"line-height: 363px;\n"
"color: #888888;\n"
"border: 0px solid #ffffff;\n"
"border-bottom:4px solid #888888;")
        self.show_text.setAlignment(QtCore.Qt.AlignCenter)
        self.show_text.setObjectName("show_text")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(131, 86, 518, 138))
        self.label_4.setStyleSheet("background: #85D2CF;\n"
"border-radius: 60px;\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 65px;\n"
"line-height: 79px;\n"
"color: #FFFFFF;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1160, -3, 761, 1011))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(200, 200))
        self.frame.setMaximumSize(QtCore.QSize(1080, 1080))
        self.frame.setStyleSheet("background: rgba(133, 210, 207, 0.27);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.keypad_6 = QtWidgets.QPushButton(self.frame)
        self.keypad_6.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_6.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_6.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" \n"
" ")
        self.keypad_6.setObjectName("keypad_6")
        self.gridLayout.addWidget(self.keypad_6, 2, 2, 1, 1)
        self.keypad_5 = QtWidgets.QPushButton(self.frame)
        self.keypad_5.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_5.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_5.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" ")
        self.keypad_5.setObjectName("keypad_5")
        self.gridLayout.addWidget(self.keypad_5, 2, 1, 1, 1)
        self.keypad_8 = QtWidgets.QPushButton(self.frame)
        self.keypad_8.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_8.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_8.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" ")
        self.keypad_8.setObjectName("keypad_8")
        self.gridLayout.addWidget(self.keypad_8, 3, 1, 1, 1)
        self.keypad_2 = QtWidgets.QPushButton(self.frame)
        self.keypad_2.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_2.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_2.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" \n"
" ")
        self.keypad_2.setObjectName("keypad_2")
        self.gridLayout.addWidget(self.keypad_2, 1, 1, 1, 1)
        self.keypad_9 = QtWidgets.QPushButton(self.frame)
        self.keypad_9.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_9.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_9.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" ")
        self.keypad_9.setObjectName("keypad_9")
        self.gridLayout.addWidget(self.keypad_9, 3, 2, 1, 1)
        self.keypad_0 = QtWidgets.QPushButton(self.frame)
        self.keypad_0.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_0.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_0.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" \n"
" ")
        self.keypad_0.setObjectName("keypad_0")
        self.gridLayout.addWidget(self.keypad_0, 4, 1, 1, 1)
        self.keypad_4 = QtWidgets.QPushButton(self.frame)
        self.keypad_4.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_4.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_4.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" ")
        self.keypad_4.setObjectName("keypad_4")
        self.gridLayout.addWidget(self.keypad_4, 2, 0, 1, 1)
        self.enter_btn = QtWidgets.QPushButton(self.frame)
        self.enter_btn.setMinimumSize(QtCore.QSize(200, 200))
        self.enter_btn.setMaximumSize(QtCore.QSize(200, 200))
        self.enter_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    background: rgba(255, 255, 255, 0);\n"
"    border-image:url(img/keypad_enter);\n"
"    padding-left:1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"QPushButton:hover {\n"
"    margin: 10px;\n"
"}\n"
" ")
        self.enter_btn.setText("")
        self.enter_btn.setObjectName("enter_btn")
        self.gridLayout.addWidget(self.enter_btn, 4, 2, 1, 1)
        self.keypad_7 = QtWidgets.QPushButton(self.frame)
        self.keypad_7.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_7.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_7.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" ")
        self.keypad_7.setObjectName("keypad_7")
        self.gridLayout.addWidget(self.keypad_7, 3, 0, 1, 1)
        self.keypad_3 = QtWidgets.QPushButton(self.frame)
        self.keypad_3.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_3.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_3.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" \n"
" ")
        self.keypad_3.setObjectName("keypad_3")
        self.gridLayout.addWidget(self.keypad_3, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.back_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setMinimumSize(QtCore.QSize(204, 134))
        self.back_btn.setMaximumSize(QtCore.QSize(204, 134))
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    background: rgba(255, 255, 255, 0);\n"
"    border-image:url(img/keypad_delate);\n"
"    padding-left:1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"QPushButton:hover {\n"
"    margin: 10px;\n"
"}\n"
" ")
        self.back_btn.setText("")
        self.back_btn.setAutoDefault(False)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 4, 0, 1, 1)
        self.keypad_1 = QtWidgets.QPushButton(self.frame)
        self.keypad_1.setMinimumSize(QtCore.QSize(200, 200))
        self.keypad_1.setMaximumSize(QtCore.QSize(200, 200))
        self.keypad_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keypad_1.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    font-family: Inter;\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 90px;\n"
"    line-height: 121px;\n"
"    color: #316866;\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background: #6e6e6e;\n"
"    color: #FFFFFF;\n"
"}\n"
" ")
        self.keypad_1.setObjectName("keypad_1")
        self.gridLayout.addWidget(self.keypad_1, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.goNextPage.setText(_translate("MainWindow", "下一步"))
        self.label_2.setText(_translate("MainWindow", "毫升"))
        self.show_text.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "注入量"))
        self.keypad_6.setText(_translate("MainWindow", "6"))
        self.keypad_5.setText(_translate("MainWindow", "5"))
        self.keypad_8.setText(_translate("MainWindow", "8"))
        self.keypad_2.setText(_translate("MainWindow", "2"))
        self.keypad_9.setText(_translate("MainWindow", "9"))
        self.keypad_0.setText(_translate("MainWindow", "0"))
        self.keypad_4.setText(_translate("MainWindow", "4"))
        self.keypad_7.setText(_translate("MainWindow", "7"))
        self.keypad_3.setText(_translate("MainWindow", "3"))
        self.keypad_1.setText(_translate("MainWindow", "1"))

