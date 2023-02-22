from PyQt5 import QtCore, QtGui, QtWidgets
from five_ui import Ui_MainWindow as five_ui_windows
from PyQt5.QtCore import QTimer, pyqtSignal


class fiveWindows(QtWidgets.QMainWindow,five_ui_windows):
    signal_list = pyqtSignal(str)
    
    def __init__(self,result,parent=None):
        super().__init__(parent)
        super(fiveWindows,self).__init__(parent)
        self.setupUi(self)
        self.label.setText("")
        self.label.setStyleSheet("border-image:url(rgb.jpg);")
        self.label_3.setText(result)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = fiveWindows()
    win.show()
    sys.exit(app.exec_())