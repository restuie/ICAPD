import sys
from PyQt5 import QtCore, QtWidgets
from one_ui_control import oneWindows
from two_ui_control import twoWindows
from three_ui_control import threeWindows
from four_ui_control import fourWindows
from five_ui_control import fiveWindows
from object_identify import _identify
import time

class controller:
    def __init__(self):
        pass

    def showOnePage(self):
        self.win1 = oneWindows()
        self.win1.signal_list.connect(self.showTwoPage)#當第一個界面的signal_list emit()後即可開啟第二個界面
        self.win1.show()

    def showTwoPage(self, injection):
        self.win2 = twoWindows(injection)
        self.win2.signal_list.connect(self.showThreePage)
        if self.win1.isActiveWindow():
            self.win1.close()
        elif self.win3.isActiveWindow():
            self.win3.close()
        self.win2.show()

    def showThreePage(self, injection):
        self.win3 = threeWindows(injection)
        self.win3.signal_list.connect(self.showTwoPage)
        self.win3.Finish_btn_2.clicked.connect(self.showFourPage)
        self.win2.close()
        self.win3.show()

    def showFourPage(self):
        self.win4 = fourWindows()
        self.win3.close()
        self.win4.show()
        time.sleep(2)
        self.Identify_Object = _identify()
        self.Identify_Object.run()
        time.sleep(2)
        print(self.Identify_Object.getResult())
        self.showFivePage(self.Identify_Object.getResult())


    def showFivePage(self,result):
        self.win4.close()
        self.win5 = fiveWindows(result)
        self.win5.show()
        self.win5.pushButton_2.clicked.connect(self.showOnePage)
        #self.win5.close()
        

    

def main():
    app = QtWidgets.QApplication(sys.argv)
    Controller = controller()
    Controller.showOnePage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
