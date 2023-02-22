from PyQt5 import QtCore, QtGui, QtWidgets
from two_ui import Ui_MainWindow as two_ui_windows
from PyQt5.QtCore import QTimer, pyqtSignal
from weigh import weigh

class twoWindows(QtWidgets.QMainWindow, two_ui_windows):
    signal_list = pyqtSignal(str)

    def __init__(self, injection, parent=None):
        super().__init__(parent)
        super(twoWindows, self).__init__(parent)
        self.setupUi(self)
        self.label_Show_Injection.setText(injection)
        self.injection = injection
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Delay2Second)
        self.timer.start(2000)
        self.heating_btn.clicked.connect(self.goToNextPage)
        self.weigh = weigh()
        self.weigh.rawdata.connect(self.showWeighData)
        self.weigh.start()
        self.weigh.runing = True


    def Delay2Second(self):
        self.heating_btn.setStyleSheet("QPushButton {\n"
                                       "    border-image:url(img/heating_btn_2.png);\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    margin: 10px;\n"
                                       "}")

    # def GetOneUIdata(self, injection):
    #     self.injection = injection
    #
    def showWeighData(self,weight):
        self.label_2.setText("{5d}".format(weight))

    def goToNextPage(self):
        # self.win3 = threeWindows()
        # self.signal_list.connect(self.win3.GetthreeUIdata)    
        self.injection = self.label_Show_Injection.text()
        self.signal_list.emit(self.injection)
        self.weigh.rawdata.disconnect()
        self.weigh.close()
        # self.close()
        # self.signal_list.disconnect()
        # self.win3.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = twoWindows()
    win.show()
    sys.exit(app.exec_())
