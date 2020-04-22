from socket import *

class cient:
    def __init__(self):
        self.serverip = "127.0.0.1"
        self.serverport = 5050
        self.buffersize = 1024

        self.client = socket(AF_INET,SOCK_STREAM)
        
    def connect(self):
        while True:
            self.client.connect((serverip,serverport))
            self.client.send(bytes(input(),"utf-8"))
            self.print(client.recv(buffersize))
            if input() == 'n':
                break
            self.client.close()
