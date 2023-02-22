from PyQt5 import QtCore, QtGui, QtWidgets
from four_ui import Ui_MainWindow as four_ui_windows
from PyQt5.QtCore import QTimer, pyqtSignal


class fourWindows(QtWidgets.QMainWindow,four_ui_windows):
    signal_list = pyqtSignal(str)
    
    def __init__(self,parent=None):
        super().__init__(parent)
        super(fourWindows,self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = fourWindows()
    win.show()
    sys.exit(app.exec_())