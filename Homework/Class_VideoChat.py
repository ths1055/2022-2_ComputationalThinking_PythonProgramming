import socket, cv2, time
import numpy as np
import threading
from queue import Queue
from _thread import*

PORT=9999

class VideoChat():
    def __init__(self, role):
        self.myRole = role
        print("VideoChat initiated as {} ...".format(role))
        hostname = socket.gethostname()
        self.myAddr = socket.gethostbyname(hostname)
        print("My IP address = {}".format(self.myAddr))
        if self.myRole == "Server":
            self.myWebCam = 1 # SERVER_WEBCAM = 0
        else:
            self.myWebCam = 0 # CLIENT_WEBCAM = 1 
        self.op_state = "RUN"
    
    def run(self):
        if self.myRole == "Server":
            self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.mySocket.bind((self.myAddr, PORT))
            self.mySocket.listen()
            print('Server::Video chatting server started')
            print('Server::Waiting for client .... ')
            self.peerSocket, self.peerAddr = self.mySocket.accept()
            print('Server::connected to client ({} : {})'.format(self.peerSocket, self.peerAddr))

        elif self.myRole == "Client":
            self.peerAddr = input("Input server IP address = ")
            print('Client::Connecting to Server')
            self.mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.mySocket.connect((self.peerAddr, PORT))
            print('Client::Connected to Server({}:{})'.format(self.peerAddr, PORT))
            self.peerSocket = self.mySocket
        
        self.queue = Queue()
        thrd_CaptureVideo = threading.Thread(target= self.captureVideo, args=(self.queue,))
        thrd_CaptureVideo.start()
        thrd_TxVideo = threading.Thread(target=self.txVideo, args=(self.peerSocket, self.peerAddr, self.queue,))
        thrd_TxVideo.start()
        thrd_RxVideo = threading.Thread(target=self.rxVideo, args=(self.peerSocket,))
        thrd_RxVideo.start()

        thrd_TxVideo.join()
        thrd_RxVideo.join()
        thrd_CaptureVideo.join()
        print("VideoChatt( {}) is closing socket and quit video chatt".format(self.myRole))
        self.mySocket.close()

    def recvall(self, sock, count):
        if count == 0 or count == None:
            return None
        buf = b""
        while count:
            try:
                newbuf = sock.recv(count)
            except:
                self.op_state = "QUIT"
                break
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def txVideo(self, peerSocket, addr, queue):
        while True:
            if self.op_state == "QUIT":
                break
            if queue.empty ():
                #print("{}::queue is empty, self.op_state = {}".format(self.myRole, self.op_state))
                time.sleep(0.1)
            try:
                stringData = queue.get()
                peerSocket.send(str(len(stringData)).ljust(16).encode())
                peerSocket.send(stringData)
            except: # ConnectionResetError, ConnectionAbortedError
                self.op_state = "QUIT"
                break
            time.sleep(0.1)
        print("{}:: closing peerSocket() ...".format(self.myRole))
        peerSocket.close()
        print("{}:: terminating thread_txVideo() ...".format(self.myRole))

    def captureVideo(self, queue):
        server_webcam = cv2.VideoCapture(self.myWebCam)
        server_webcam.set(cv2.CAP_PROP_FPS, 30) # change FPS from 30 to 8
        fr_width, fr_height, fps = server_webcam.get(3), server_webcam.get(4), server_webcam.get(cv2.CAP_PROP_FPS)
        print("{}_webcam frame width ({}), height({}), fps({})".format(self.myRole, fr_width, fr_height, fps))
        while True:
            if self.op_state == "QUIT":
                break
            ret, serv_frame = server_webcam.read()
            if ret == False:
                continue
            resized_svrfr = cv2.resize(serv_frame, (int(serv_frame.shape[1]/2), int(serv_frame.shape[0]/2)))
            encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
            result, imgencode = cv2.imencode('.jpg', resized_svrfr, encode_param)
            img_data = np.array(imgencode)
            stringData = img_data.tobytes()
            queue.put(stringData)
            #cv2.imshow('Server:: Resized_Server_Video', resized_svrfr)
            key = cv2.waitKey(1)
            if key == 27: # if ESC key is input, then exit
                print("{} :: ESC key pressed => exit".format(self.myRole))
                self.op_state = "QUIT"
                break
            time.sleep(0.05)
        print("{}:: terminating thread_captureVideo() ...".format(self.myRole))
      
    def rxVideo (self, peerSocket):
        while True:
            if self.op_state == "QUIT":
                break
            length = self.recvall (peerSocket, 16)
            if length == 0 or length == None or length == b'':
                self.op_state = "QUIT"
                break
            stringData = self.recvall(peerSocket, int(length))
            data = np.frombuffer(stringData, dtype='uint8')
            decimg=cv2.imdecode(data,1)
            cv2.imshow('{} :: received video from peer'.format(self.myRole),decimg)
            key = cv2.waitKey(1)
            if key == 27: # if ESC key is input, then exit
                print("{} :: ESC key pressed => exit".format(self.myRole))
                self.op_state = "QUIT"
                break
            time.sleep(0.05)
        print("{}:: terminating thread_rxVideo() ...".format(self.myRole))