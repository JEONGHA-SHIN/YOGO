from threading import *
from socket import *
from PyQt5.QtCore import Qt, pyqtSignal, QObject
import cv2
import numpy
from queue import Queue
queue = Queue()

class Signal(QObject):
    recv_signal = pyqtSignal(str)
    disconn_signal = pyqtSignal()


class ClientSocket:

    def __init__(self, parent):
        self.parent = parent

        self.recv = Signal()
        self.recv.recv_signal.connect(self.parent.updateMsg)
        self.disconn = Signal()
        self.disconn.disconn_signal.connect(self.parent.updateDisconnect)

        self.bConnect = False

    def __del__(self):
        self.stop()

    def connectServer(self, ip, port):
        self.client = socket(AF_INET, SOCK_STREAM)

        try:
            self.client.connect((ip, port))
        except Exception as e:
            print('Connect Error : ', e)
            return False
        else:
            self.bConnect = True
            self.t = Thread(target=self.receive, args=(self.client,))
            self.t.start()
            print('Connected')

        return True

    def stop(self):
        self.bConnect = False
        if hasattr(self, 'client'):
            self.client.close()
            del (self.client)
            print('Client Stop')
            self.disconn.disconn_signal.emit()

    def receive(self, client):
        while self.bConnect:
            try:
                recv = client.recv(1024)
            except Exception as e:
                print('Recv() Error :', e)
                break
            else:
                msg = str(recv, encoding='utf-8')
                if msg:
                    self.recv.recv_signal.emit(msg)
                    print('[RECV]:', msg)

        self.stop()

    def send(self, msg):
        if not self.bConnect:
            return

        try:
            self.client.send(str(len(msg)).ljust(16).encode())
            self.client.send(msg) #.encode()
        except Exception as e:
            print('Send() Error : ', e)
        print(msg)
        print(type(msg))


    def webcam(self):

        capture = cv2.VideoCapture(0)


        ret, frame = capture.read()

        #if ret == False:
        #    continue

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)

        data = numpy.array(imgencode)
        stringData = data.tostring()
        queue.put(stringData)

        cv2.imshow('image', frame)

        key = cv2.waitKey(1)

        return stringData