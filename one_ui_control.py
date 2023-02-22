from one_ui import Ui_MainWindow as one_ui_windows
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from two_ui_control import twoWindows


class oneWindows(QtWidgets.QMainWindow, one_ui_windows):
    signal_list = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        super(oneWindows, self).__init__(parent)
        self.setupUi(self)
        self.injection = ''
        self.keypad_1.clicked.connect(lambda: self.keyword("1"))
        self.keypad_2.clicked.connect(lambda: self.keyword("2"))
        self.keypad_3.clicked.connect(lambda: self.keyword("3"))
        self.keypad_4.clicked.connect(lambda: self.keyword("4"))
        self.keypad_5.clicked.connect(lambda: self.keyword("5"))
        self.keypad_6.clicked.connect(lambda: self.keyword("6"))
        self.keypad_7.clicked.connect(lambda: self.keyword("7"))
        self.keypad_8.clicked.connect(lambda: self.keyword("8"))
        self.keypad_9.clicked.connect(lambda: self.keyword("9"))
        self.keypad_0.clicked.connect(lambda: self.keyword("0"))
        self.back_btn.clicked.connect(lambda: self.keyword_back())
        self.goNextPage.clicked.connect(lambda: self.goToNextPage())
        self.goNextPage.setEnabled(False)

        # self.goNextPage.clicked.connect()

    def keyword(self, number):
        s = self.show_text.text()
        if (s == "0" or len(s) >= 4):
            self.show_text.setText(number)
            s = number
            self.goNextPage.setEnabled(False)
        elif (self.show_text.text() != "0" and len(s) < 4):
            self.show_text.setText(s+number)
        if (s != "0"):
            self.goNextPage.setEnabled(True)

    def keyword_back(self):
        s = self.show_text.text()
        if (len(s) > 1):
            s = s[:-1]
            self.show_text.setText(s)
            self.goNextPage.setEnabled(True)
        elif (len(s) == 1):
            self.goNextPage.setEnabled(False)
            s = "0"
            self.show_text.setText(s)

    def goToNextPage(self):
        # self.win2 = twoWindows()
        # self.signal_list.connect(self.win2.GetOneUIdata)
        self.injection = self.show_text.text()
        self.signal_list.emit(self.injection)
        # self.signal_list.disconnect()
        # self.win2.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = oneWindows()
    win.show()
    sys.exit(app.exec_())
