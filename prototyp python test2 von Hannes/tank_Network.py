import pickle
import socket

#dd
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.2.108" # hier ip adresse einfügen
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()


    def getP(self): #damit pplayer dinge übertragen werden
        return self.p


#connection überprüfung
    def connect(self): #connction
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(8192))
        except:
            pass
#senden daten
    def send(self, data): #pickle von daten

        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(8192))
        except socket.error as e:
            print(e)