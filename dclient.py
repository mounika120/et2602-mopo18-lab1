import select
import socket
import sys
import time
import errno
import threading
import queue
class client_socket:
    def __init__(self):
        try:
            self.client_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print('socket has been created')
        except socket.error :
            print('Sockets not created')
            sys.exit()
        self.host = sys.argv[1]
        self.port = int(sys.argv[2])
        self.nick_name = sys.argv[3]
        if(len(sys.argv)!=4):
            sys.exit()
        try:
            self.client_.connect((self.host,self.port))
            print('client has been  connected')
        except socket.error :
            print('server not found')
            sys.exit()
        self.nick_name = bytes(self.nick_name ,'utf-8')
        self.client_.send(self.nick_name)
        self.client_.setblocking(1)
    def recvdata(self):
        while True:
            try:
                data = self.client_.recv(1024)
                if (len(data)!=0):
                    msg = data.decode('utf-8')
                    print(msg)
                    time.sleep(0.1)
            except IOError:
                continue
    def inputdata(self):
        try:
            data = input()
            data1 = data.strip('MSG')
            data = bytes(data,'utf-8')
            try:
                self.client_.send(data)
                if data1 == ' quit':
                    print("client has been succesfully disconnected")
                    self.client_.close()
                    sys.exit(1)
                time.sleep(0.1)
            except:
                pass
        except IOError:
            pass
    def run_client(self):
        t1 = threading.Thread(target = self.recvdata)
        t1.start()
        while True:
            self.inputdata()
def main():
    client_obj = client_socket()
    client_obj.run_client()
if __name__ == "__main__":
    main()
