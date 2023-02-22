from PyQt5 import QtCore, QtGui, QtWidgets
from three_ui import Ui_MainWindow as three_ui_windows
from PyQt5.QtCore import QTimer, QPropertyAnimation, QSize, QRect, QEasingCurve, QThread, pyqtSignal
from PyQt5.QtWidgets import QGraphicsBlurEffect
from mlx90614 import MLX90614
import time
from smbus2 import SMBus



class threeWindows(QtWidgets.QMainWindow, three_ui_windows):
    signal_list = pyqtSignal(str)

    def __init__(self, injection='5000', parent=None):
        super().__init__(parent)
        super(threeWindows, self).__init__(parent)
        self.setupUi(self)
        self.frame_5.hide()
        #self.Finish_btn.setEnabled(False)
        #self.Finish_btn.hide()
        self.label_Show_Injection.setText(injection)
        self.label_Show_Injection_2.setText(injection)
        self.animation = QPropertyAnimation(self.heating_scroll, b'geometry')
        self.animation2 = QPropertyAnimation(self.frame_2, b'geometry')
        self.animation3 = QPropertyAnimation(self.frame_4, b'geometry')

        # self.worker = worker()
        # self.worker.sinout.connect(self.PlayAnimation)
        # self.worker.start()

        self.readTemp = readTemp()
        self.readTemp.rawdata.connect(self.showTemp)
        self.readTemp.start()
        self.readTemp.runing = True

        self.stopheating.clicked.connect(self.goToBackPage)
        self.Finish_btn.clicked.connect(self.show_identify_panel)

    def PlayAnimation(self, time):
        print(time)
        if (time < 16):
            self.PlayHeatingAnimation(time)
        elif (time >= 16):
            self.PlayInjectionAnimation(time)
        if (time >= 31):
            self.Finish_btn.setEnabled(True)
            self.Finish_btn.show()

    def PlayInjectionAnimation(self, time):
        x = (time-16) * 30
        x1 = (time-16+1) * 30
        self.animation3.setDuration(900)
        # self.animation.setKeyValueAt(QRect(0, 480, 770, 220))
        # self.animation.setKeyValueAt(QRect(0, 0, 770, 700))
        self.animation3.setStartValue(QRect(0, 0, 770, 220+x))
        self.animation3.setEndValue(QRect(0, 0, 770, 220+x1))
        self.animation3.setEasingCurve(QEasingCurve.Linear)  # 動畫緩動曲線
        # # self.animation.setLoopCount(-1) #重複播放
        self.animation3.start()

        # x+y=700
        # 22->37 1/15

        # self.heating_scroll.setGeometry(QtCore.QRect(0, x, 770, 700-x))
    def PlayHeatingAnimation(self, time):
        x = 480 - (time) * 30
        x1 = 480 - (time+1) * 30
        self.label_Show_Temp.setText(str(time + 22))
        self.label_Show_Temp_2.setText(str(time + 22))
        self.animation.setDuration(900)
        self.animation2.setDuration(900)
        # self.animation.setKeyValueAt(QRect(0, 480, 770, 220))
        # self.animation.setKeyValueAt(QRect(0, 0, 770, 700))
        self.animation.setStartValue(QRect(0, x, 770, 700-x))
        self.animation.setEndValue(QRect(0, x1, 770, 700-x1))
        self.animation2.setStartValue(QRect(0, 0, 770, x))
        self.animation2.setEndValue(QRect(0, 0, 770, x1))
        self.animation.setEasingCurve(QEasingCurve.Linear)  # 動畫緩動曲線
        self.animation2.setEasingCurve(QEasingCurve.Linear)
        # # self.animation.setLoopCount(-1) #重複播放
        self.animation.start()
        self.animation2.start()

    def showTemp(self,temp):
        self.label_Show_Temp.setText("{0:>5.2f}".format(temp))

    def goToBackPage(self):
        self.injection = self.label_Show_Injection.text()
        self.signal_list.emit(self.injection)

    def goToNextPage(self):
        pass
    
    def show_identify_panel(self):
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(10)
        self.blur_effect.setBlurHints(QGraphicsBlurEffect.PerformanceHint)
        self.frame_6.setGraphicsEffect(self.blur_effect)
        self.frame_5.show()


class worker(QThread):
    sinout = pyqtSignal(int)
    def __init__(self, parent=None):
        super(worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        for i in range(0, 32):
            self.sinout.emit(i)
            time.sleep(1)

class readTemp(QThread):
    rawdata=QtCore.pyqtSignal(float)
    def __init__(self,parent=None):
        super(readTemp,self).__init__(parent)
        self.runing=False
        self.thermometer_address=0x5a
        self.bus = SMBus(1)
        self.sensor = MLX90614(self.bus,address=self.thermometer_address)


    def run(self):
        while self.runing:
            try:
                object_temp = self.sensor.get_obj_temp()
                self.rawdata.emit(object_temp)
                time.sleep(1)
            except IOError:
                print('Mlx90614 not connect')
    def open(self):
        self.runing = True
        print("Mlx90614 open")
    def close(self):
        self.runing = False
        self.bus.close()
        print("Mlx90614 close")

    def stop(self):
        self.runing = False
        print("Mlx90614 stop")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = threeWindows()
    win.show()
    sys.exit(app.exec_())
