# -*- coding: utf-8 -*-


# ##########
# Author:Dynais
#
# Describe: This is a Pomodora Timer Application
#
#
# ###########


# 系统包
import sys
import os
import time
import json
from playsound import playsound
from imutils.video import VideoStream
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

# 自己的包
from ui.mainwindow import Ui_MainWindow
from ui.breakwindow import Ui_BreakWindow
from ui.timeinputdialog import Ui_TimeInputDialog
from ui.helpdialog import Ui_HelpDialog
from ui.aboutdialog import Ui_AboutDialog
from ui.facewindow import Ui_FaceWindow
import tools
import detect_faces_video


# 窗口类定义
class MainWindow(QMainWindow):
    # 定义一个倒计时结束的信号

    def __init__(self):
        """初始化参数以及设置窗口ui
                """
        super().__init__()
        global config

        # UI设置
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Pomodoro v0.6")
        self.setWindowIcon(QIcon("image/tomato.png"))
        # 设置Start按钮可用, Reset按钮不可用
        self.ui.button_start.setEnabled(True)
        self.ui.button_reset.setEnabled(False)
        # 时间相关参数设置
        self.timer = QTimer()
        self.timeInit()

        #子窗口建立
        self.subBreak = BreakWindow(self)
        self.subTimeSetting = TimeSettingDialog(self)
        self.subHelp = HelpDialog(self)
        self.subAbout = AboutDialog(self)
        self.subFaceWindow = FaceWindow(self)

        # 触发区
        self.ui.button_start.clicked.connect(self.start)
        self.ui.button_reset.clicked.connect((self.reset))

        self.timer.timeout.connect(self.timeProcess)

        self.ui.actionTime_Setting.triggered.connect(self.subTimeSetting.show) # 绑定按钮Time_Setting到函数
        self.ui.actionAlarm.triggered.connect(self.debug)  # 绑定按钮Alarm到函数
        self.ui.actionShow_Data.triggered.connect(self.debug)  # 绑定按钮Show_Data到函数
        self.ui.actionShow_List.triggered.connect(self.debug)  # 绑定按钮Show_List到函数
        self.ui.actionHelp.triggered.connect(self.subHelp.show)  # 绑定按钮Help到函数
        self.ui.actionAbout.triggered.connect(self.subAbout.show)  # 绑定按钮About到函数
        self.ui.actionFace_Detect.triggered.connect((self.subFaceWindow.show))


    def timeProcess(self):
        """计时器中断触发的倒计时进程
        """
        if self.isTimeOut():
            self.timer.stop()
            playsound("sound/ring.mp3")
            # 呼出子窗口
            self.subBreak.start()
            # 重置番茄
            self.reset()
        else :
            # 如果打开了检测人脸按钮, 那么加入人脸判断
            if self.subFaceWindow.ISACTIVE and self.subFaceWindow.IFCAM:
                # 进行一次检测
                self.subFaceWindow.faceDetect()
                # 如果没有检测到人脸, 就放弃当前番茄, 否则正常进行
                if not self.subFaceWindow.IFFACE:
                    self.reset()
                else:
                    self.timeUpdate()

                # 如果打开了debug模式且窗口没有隐藏, 则可以看到图像
                if self.subFaceWindow.ISDEBUG and not self.subFaceWindow.isHidden() and self.subFaceWindow.IFCAM:
                    self.subFaceWindow.imshow(self.subFaceWindow.capFrame)
            else:
                self.timeUpdate()



    def timeInit(self):
        """尝试初始化时间参数并更新时间标签
        """
        if self.timer.isActive():
            self.timer.stop()
        try:
            self.timeTarget = config["tomato"]["t_target"]
        except:
            print("init errow!")
            self.timeTarget = "99:99"
        finally:
            self.timeStart = time.time()
            self.timeNow = time.time()
            self.ui.label_time.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
                    self.timeTarget))


    def timeUpdate(self):
        """更新时间标签
        """
        self.timeNow = time.time()
        if tools.tomato2sec(self.timeTarget) - (self.timeNow - self.timeStart) >= 0:
            self.ui.label_time.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
                    tools.sec2tomato(tools.tomato2sec(self.timeTarget) - (self.timeNow - self.timeStart))))
            QApplication.processEvents()


    def isTimeOut(self):
        """判断倒计时是否结束
            Returns:
                Bool 表示时间是否结束
        """
        if tools.tomato2sec(self.timeTarget) - (self.timeNow - self.timeStart) <= 0:
            return True
        else:
            return False


    def start(self):
        """开始一个番茄, 已经开始番茄的状态下不可点击
        """
        # 同时间只能开一个timer
        if self.timer.isActive():
            return
        # 时间初始化
        self.timeInit()
        self.timer.start(100)
        # 设置Start按钮不可用, Reset按钮可用
        self.ui.button_start.setEnabled(False)
        self.ui.button_reset.setEnabled(True)


    def reset(self):
        """重置整个番茄界面
        """
        self.timeInit()
        # 设置Start按钮可用, Reset按钮不可用
        self.ui.button_start.setEnabled(True)
        self.ui.button_reset.setEnabled(False)


    def debug(self):
        """保留debug函数

                        Args:
                            None

                        Returns:
                            None

                        Raises:
                            None
                """
        print("debuging...")


class BreakWindow(QDialog):
    def __init__(self,parent=None):
        """初始化参数以及设置窗口ui

               Args:
                   None

               Returns:
                   None

               """
        super().__init__(parent)
        self.ui = Ui_BreakWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Free Time...")
        self.setWindowIcon(QIcon("image/free.png"))

        # 时间参数初始化
        self.timer = QTimer()
        self.timeInit()

        # 触发区
        self.ui.button_nTomato.clicked.connect(self.quit)
        self.timer.timeout.connect(self.timeProcess)


    def timeProcess(self):
        """倒计时进程
        """

        if self.isTimeout():
            self.timer.stop()
            playsound("sound/ring.mp3")
            # 退出休息
            self.quit()
        else:
            self.timeUpdate()


    def timeInit(self):
        """初始化时间

               Args:
                   None

               Returns:
                   None

               """
        if self.timer.isActive():
            self.timer.stop()
        try:
            self.bTimeTarget = config["tomato"]["t_break"]
        except:
            print("init errow!")
            self.bTimeTarget = "99:99"
        finally:
            self.bTimeStart = time.time()
            self.bTimeNow = time.time()
            self.ui.label_break.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
                    self.bTimeTarget))


    def timeUpdate(self):
        """更新时间标签
                """
        self.bTimeNow = time.time()
        if tools.tomato2sec(self.bTimeTarget) - (self.bTimeNow - self.bTimeStart) >= 0:
            self.ui.label_break.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
                    tools.sec2tomato(tools.tomato2sec(self.bTimeTarget) - (self.bTimeNow - self.bTimeStart))))
            QApplication.processEvents()


    def isTimeout(self):
        """判断倒计时是否结束
            Returns:
                Bool 表示时间是否结束
                 """
        if tools.tomato2sec(self.bTimeTarget) - (self.bTimeNow - self.bTimeStart) <= 0:
            return True
        else:
            return False


    def start(self):
        """开始循环时钟
        """
        self.show()
        # 同时间只能开一个timer
        if self.timer.isActive():
            return
        # 时间初始化
        self.timeInit()
        self.timer.start(100)


    def quit(self):
        self.timeInit()
        window.start()
        self.hide()


    def closeEvent(self, QCloseEvent):
        self.quit()
        window.reset()


    def debug(self):
        """保留debug函数

               Args:
                   None

               Returns:
                   None

               """
        print("debuging...")


class TimeSettingDialog(QDialog):
    def __init__(self,parent=None):
        """初始化参数以及设置窗口ui

               Args:
                   None

               Returns:
                   None

               Raises:
                   None
               """
        super().__init__(parent)
        global config
        self.ui = Ui_TimeInputDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Time Settings")
        self.setWindowIcon(QIcon("image/tomato.png"))

        # 保留参数
        try:
            self.ui.timeEdit_target.setTime(tools.tomato2Qtime(config["tomato"]["t_target"]))
            self.ui.timeEdit_break.setTime(tools.tomato2Qtime(config["tomato"]["t_break"]))
        except:
            print("init errow!")
            pass
        finally:
            pass

        # 触发区
        self.ui.buttonBox.accepted.connect(self.saveData)
        self.ui.buttonBox.rejected.connect(self.close)


    def saveData(self):
        """保存设置窗口的数据, 并进行一次主窗口的初始化, 如果休息窗口此时可见, 同时对休息窗口也进行一次初始化

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        targetTime = self.ui.timeEdit_target.time().minute()*60 + self.ui.timeEdit_target.time().second()
        breakTime = self.ui.timeEdit_break.time().minute()*60 + self.ui.timeEdit_break.time().second()

        if not targetTime == 0:
            config["tomato"]["t_target"] = tools.sec2tomato(targetTime)
        if not breakTime == 0:
            config["tomato"]["t_break"] = tools.sec2tomato(breakTime)

        # 读取配置文件
        with open("config.json", "w") as c:
            json.dump(config, c)

        # 进行一次初始化
        window.reset()
        self.close()


    def debug(self):
        """保留debug函数
        """
        print("debuging...")


class HelpDialog(QDialog):

    # 初始化参数以及设置窗口ui
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_HelpDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Help")
        self.setWindowIcon(QIcon("image/tomato.png"))


class AboutDialog(QDialog):
    # 初始化参数以及设置窗口ui
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Help")
        self.setWindowIcon(QIcon("image/tomato.png"))


class FaceWindow(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_FaceWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Face Window")
        self.setWindowIcon(QIcon("image/tomato.png"))
        self.ISDEBUG = False
        self.ISACTIVE = False
        self.IFFACE = True
        self.IFCAM = False
        self.ui.checkBoxOpenDebug.setChecked(False)
        self.ui.checkBoxOpenDetect.setChecked(False)

        # load our serialized model from disk
        print("[INFO] loading model...")
        try:
            self.net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
        except:
            print("[INFO] Missing model!!!")
            sys.exit()

        self.ui.checkBoxOpenDetect.stateChanged.connect(self.flagInit)
        self.ui.checkBoxOpenDebug.stateChanged.connect(self.flagInit)


    def flagInit(self):
        self.ISDEBUG = self.ui.checkBoxOpenDebug.isChecked()
        self.ISACTIVE = self.ui.checkBoxOpenDetect.isChecked()
        if self.ISACTIVE and not self.IFCAM:
            try:
                print("[INFO] starting video stream...")
                self.vs = VideoStream(src=0).start()
                self.IFCAM = True
                time.sleep(1.0)
            except:
                print("[INFO] Missing camera!!!")
                self.ui.checkBoxOpenDetect.setChecked(False)
        elif not self.ISACTIVE and self.IFCAM:
            try:
                print("[INFO] stopping video stream...")
                self.vs = VideoStream(src=0).stop()
                time.sleep(1.0) 
                self.IFCAM = False
            except:
                print("[INFO] Missing camera!!!")




    def faceDetect(self):
        self.IFFACE, self.capFrame = detect_faces_video.ifFace(self.vs, self.net)
        print(self.IFFACE)


    def imshow(self, capFrame):
        img = capFrame  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        # self.zoomscale = 1  # 图片放缩尺度
        self.frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(self.frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)


    def closeEvent(self, QCloseEvent):
        self.hide()


# ------------ 系统初始化 ------------
if __name__ == '__main__':
    with open("config.json", "r") as c:
        config = json.load(c)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
