import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.2.108" # WICHTIG: hier müsst ihr eure locale ip adresse einfügen
        self.port = 5555  # port mit welchen hier verbunden wird (ruter abhängig kann sein das es ein anderer ist)
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


n = Network()
print(n.send("hallo du geile sau "))  #test nachrichten die an denn server gesendet werden
print(n.send("ey eumel"))           # auch eine test nachricht


#1. Run the Server.py
#2. Run the Network.py