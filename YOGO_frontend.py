# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YOGO_frontend.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import client
from PyQt5 import QtCore, QtGui, QtWidgets
from _thread import *
import cv2
import numpy
from ur3 import ur3
import robotiq_gripper_2F as gp
import subprocess

import time
from queue import LifoQueue


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
#queue = LifoQueue()


class Ui_MainWindow(object):

    def __init__(self):
        #super().__init__()
        self.c = client.ClientSocket(self)
        self.queue = client.queue
        self.rb = ur3()
        self.i = 0
        self.box_on = 0
        start_new_thread(self.webcam, (self.queue,))
        self.obj_list = [[0] * 6 for _ in range(5)]


        self.setupUi(MainWindow)

    def __del__(self):
        self.c.stop()
        self.rb.close()
        gp.closeSerial()
        print(1)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 710)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.camera_view = QtWidgets.QGroupBox(self.centralwidget)
        self.camera_view.setMinimumSize(QtCore.QSize(720, 480))
        self.camera_view.setObjectName("camera_view")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.camera_view)
        self.gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame = QtWidgets.QLabel(self.camera_view)
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.frame.resize(720, 480)
        self.frame.setScaledContents(True)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.camera_view, 0, 0, 1, 1)
        self.tab_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_3.setObjectName("tab_3")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_5.setObjectName("gridLayout_5")


        self.groupBox_2 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0)
        self.txt_yogo_ip = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_yogo_ip.setObjectName("txt_yogo_ip")
        self.gridLayout_2.addWidget(self.txt_yogo_ip, 0, 1)
        self.btn_yogo_connect = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_yogo_connect.setObjectName("btn_yogo_connect")
        self.gridLayout_2.addWidget(self.btn_yogo_connect, 0, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0)
        self.txt_yogo_portt = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_yogo_portt.setObjectName("txt_yogo_portt")
        self.gridLayout_2.addWidget(self.txt_yogo_portt, 1, 1)
        self.btn_yogo_disconnect = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_yogo_disconnect.setObjectName("btn_yogo_disconnect")
        self.gridLayout_2.addWidget(self.btn_yogo_disconnect, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.groupBox_3 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0)
        self.txt_robot_ip = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_robot_ip.setObjectName("txt_robot_ip")
        self.gridLayout_3.addWidget(self.txt_robot_ip, 0, 1)
        self.btn_robot_connect = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_robot_connect.setObjectName("btn_robot_connect")
        self.gridLayout_3.addWidget(self.btn_robot_connect, 0, 2)
        self.btn_robot_disconnect = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_robot_disconnect.setObjectName("btn_robot_disconnect")
        self.gridLayout_3.addWidget(self.btn_robot_disconnect, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0)
        self.txt_robot_portt = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_robot_portt.setObjectName("txt_robot_portt")
        self.gridLayout_3.addWidget(self.txt_robot_portt, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 1, 0, 1, 1)


        self.groupBox_4 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.txt_gripper_port = QtWidgets.QLineEdit(self.groupBox_4)
        self.txt_gripper_port.setObjectName("txt_gripper_port")
        self.gridLayout_4.addWidget(self.txt_gripper_port, 0, 1)
        self.btn_gripper_connect = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_gripper_connect.setObjectName("btn_gripper_connect")
        self.gridLayout_4.addWidget(self.btn_gripper_connect, 0, 2)
        self.btn_gripper_disconnect = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_gripper_disconnect.setObjectName("btn_gripper_disconnect")
        self.gridLayout_4.addWidget(self.btn_gripper_disconnect, 1, 2)
        self.txt_gripper_baudrate = QtWidgets.QLineEdit(self.groupBox_4)
        self.txt_gripper_baudrate.setObjectName("txt_gripper_baudrate")
        self.gridLayout_4.addWidget(self.txt_gripper_baudrate, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0  )


        self.gridLayout_5.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.tab_3.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.grip = QtWidgets.QPushButton(self.tab2)
        self.grip.setObjectName("grip")
        self.gridLayout_6.addWidget(self.grip, 3, 0, 1, 1)
        self.btn_manual = QtWidgets.QPushButton(self.tab2)
        self.btn_manual.setObjectName("btn_manual")
        self.gridLayout_6.addWidget(self.btn_manual, 2, 0, 1, 1)
        self.listView = QtWidgets.QListWidget(self.tab2)
        self.listView.setObjectName("listView")
        self.gridLayout_6.addWidget(self.listView, 1, 0, 1, 1)
        self.btn_detect = QtWidgets.QPushButton(self.tab2)
        self.btn_detect.setObjectName("btn_detect")
        self.gridLayout_6.addWidget(self.btn_detect, 0, 0, 1, 1)
        self.tab_3.addTab(self.tab2, "")
        self.gridLayout_8.addWidget(self.tab_3, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.dialog = QtWidgets.QTextBrowser(self.groupBox)
        self.dialog.setMinimumSize(QtCore.QSize(0, 120))
        self.dialog.setObjectName("dialog")
        self.gridLayout.addWidget(self.dialog, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox, 1, 0, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_yogo_connect.clicked.connect(self.yogo_connectClicked)
        self.btn_detect.clicked.connect(self.sendMsg)
        self.btn_yogo_disconnect.clicked.connect(self.yogo_disconnectClicked)

        self.btn_robot_connect.clicked.connect(self.robot_connectClicked)
        self.btn_robot_disconnect.clicked.connect(self.robot_disconnectClicked)

        self.btn_gripper_connect.clicked.connect(self.gripper_connectClicked)
        self.btn_gripper_disconnect.clicked.connect(self.gripper_disconnectClicked)
        self.grip.clicked.connect(self.grip_Clicked)

        self.btn_manual.clicked.connect(self.manual_Clicked)



        self.retranslateUi(MainWindow)
        self.tab_3.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.camera_view.setTitle(_translate("MainWindow", "Camera"))
        self.groupBox_2.setTitle(_translate("MainWindow", "YOGO"))
        self.label.setText(_translate("MainWindow", "IP"))
        self.txt_yogo_ip.setText(_translate("MainWindow", "141.223.65.209"))
        self.btn_yogo_connect.setText(_translate("MainWindow", "Connect"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.txt_yogo_portt.setText(_translate("MainWindow", "3000"))
        self.btn_yogo_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Robot"))
        self.label_3.setText(_translate("MainWindow", "IP"))
        self.txt_robot_ip.setText(_translate("MainWindow", "192.168.0.34"))
        self.btn_robot_connect.setText(_translate("MainWindow", "Connect"))
        self.btn_robot_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_4.setText(_translate("MainWindow", "Port"))
        self.txt_robot_portt.setText(_translate("MainWindow", "3000"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Gripper"))
        self.txt_gripper_port.setText(_translate("MainWindow", "COM7"))
        self.btn_gripper_connect.setText(_translate("MainWindow", "Connect"))
        self.btn_gripper_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.txt_gripper_baudrate.setText(_translate("MainWindow", "115200"))
        self.label_5.setText(_translate("MainWindow", "COM Port"))
        self.label_6.setText(_translate("MainWindow", "Baudrate"))
        self.tab_3.setTabText(self.tab_3.indexOf(self.tab1), _translate("MainWindow", "Configuration"))
        self.grip.setText(_translate("MainWindow", "GRIP!"))
        self.btn_manual.setText(_translate("MainWindow", "Manual Detect"))
        self.btn_detect.setText(_translate("MainWindow", "DETECT"))
        self.tab_3.setTabText(self.tab_3.indexOf(self.tab2), _translate("MainWindow", "Working"))
        self.groupBox.setTitle(_translate("MainWindow", "Dialog"))

    def yogo_connectClicked(self):
        if self.c.bConnect == False:
            ip = self.txt_yogo_ip.text()
            port = self.txt_yogo_portt.text()
            if self.c.connectServer(ip, int(port)):
                self.dialog.append('Connected to server')
                #print('연결 완료')
            else:
                self.c.stop()
                self.dialog.append('Disconnected from server')
                #print('연결 끊김')
        else:
            self.c.stop()
            self.dialog.append('Disconnected from server')
            #print('연결 끊김')

    def yogo_disconnectClicked(self):
        self.c.stop()
        self.dialog.append('Disconnected from server')
        #print("서버 연결 종료")

    def robot_connectClicked(self):
        bind_ip = self.txt_robot_ip.text()
        self.rb.connect(bind_ip)
        self.dialog.append("Robot connected")
        self.dialog.append("WARNING: Robot will move!!")
        #print("Robot connected!!")
        #print("WARNING: Robot will move!!!")

    def robot_disconnectClicked(self):
        self.rb.close()

    def gripper_connectClicked(self):
        port = self.txt_gripper_port.text()
        br = self.txt_gripper_baudrate.text()
        gp.init(port)
        gp.setPosition(0)

    def gripper_disconnectClicked(self):
        gp.closeSerial()

    def grip_Clicked(self):
        #obj = self.listView.currentItem().text()
        #txt = "Try to grip " + str(obj)
        tcp = [[0, 0, 0, 0, 0, 0]]

        self.rb.go_2_bin(tcp)
        time.sleep(5)
        self.rb.go_down(0.07)
        time.sleep(0.5)
        gp.setPosition(200, 50)
        time.sleep(1)
        self.rb.go_down(-0.05)
        time.sleep(0.5)
        self.rb.go_destination()
        time.sleep(3)
        gp.setPosition(0, 100)



    def sendMsg(self):
        print("")
        # self.c.send()
        # self.dialog.append("detecting objects...")
        # self.listView.clear()
        # self.box_on = 1
        #print("사진 전송")
        #self.sendmsg.clear()

    def updateMsg(self, msg): #tag1
        print(msg)
        msg_list = msg.split("b'")
        k = int(msg_list[0])
        self.obj_list = [[0] * 6 for _ in range(k)]
        self.dialog.append(str(k) + " objects are detected!")
        for i in range(k):
            tmp = msg_list[i + 1].split("/")
            self.obj_list[i][0] = tmp[0].strip("'")
            self.obj_list[i][1] = float(tmp[1])
            tmp2 = tmp[2].split(",")
            self.obj_list[i][2] = float(tmp2[0].lstrip("("))
            self.obj_list[i][3] = float(tmp2[1])
            self.obj_list[i][4] = float(tmp2[2])
            self.obj_list[i][5] =float(tmp2[3].strip(")"))
            #self.obj_list[i][2] = tmp3
            self.listView.addItem(self.obj_list[i][0])


    def updateDisconnect(self):
        self.c.stop()
        #print("접속끊김")


    def webcam(self, queue):

        capture = cv2.VideoCapture(1)
        #capture.set(3,416)
        #capture.set(4,416)


        while True:
            ret, frame = capture.read()

            if ret == False:
                continue

            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, imgencode = cv2.imencode('.jpg', frame, encode_param)

            data = numpy.array(imgencode)
            stringData = data.tostring()

            queue.put(stringData)

            cam = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cam = cv2.resize(cam, (416, 416), interpolation=cv2.INTER_LINEAR)
            if self.box_on == 1:
                cam = self.cvDrawBoxes(self.obj_list, cam)
            img = QImage(cam, cam.shape[1], cam.shape[0], QImage.Format_RGB888)  # , frame.shape[1], frame.shape[0], QImage.Fromat_RGB888
            pix = QPixmap.fromImage(img)
            self.frame.setPixmap(pix)

            key = cv2.waitKey(1)
            if key == 27:
                break

    def convertBack(self, x, y, w, h):
        xmin = int(round(x - (w / 2)))
        xmax = int(round(x + (w / 2)))
        ymin = int(round(y - (h / 2)))
        ymax = int(round(y + (h / 2)))
        return xmin, ymin, xmax, ymax

    def cvDrawBoxes(self, detections, img):
        num = len(detections)
        for a in range(num):
            x = detections[a][2]
            y = detections[a][3]
            w = detections[a][4]
            h = detections[a][5]
            # x, y, w, h = detection[2][0], \
            #              detection[2][1], \
            #              detection[2][2], \
            #              detection[2][3]
            xmin, ymin, xmax, ymax = self.convertBack(float(x), float(y), float(w), float(h))
            pt1 = (xmin, ymin)
            pt2 = (xmax, ymax)
            cv2.rectangle(img, pt1, pt2, (0, 255, 0), 1)
            # cv2.putText(img,
            #             detection[0] +
            #             " [" + str(round(detection[1] * 100, 2)) + "]",
            #             (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
            #             [0, 255, 0], 2)
        return img

    def manual_Clicked(self):
        print("")
        #subprocess.call("python","takeROI.py")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

