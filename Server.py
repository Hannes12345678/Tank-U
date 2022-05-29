import socket
from _thread import *
import sys


server = "192.168.2.108"  # WICHTIG: hier müsst ihr eure locale ip adresse einfügen
port = 5555  # port mit welchen hier verbunden wird (ruter abhängig kann sein das es ein anderer ist)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)  # die zahl bestimmt wie viele leute Connecten können, hier 2
print("Warte auf Verbindung, Server wurde gestartet")


def threaded_client(conn):
    conn.send(str.encode("Verbunden"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply= data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Verbindung abgebrochen")
    conn.close()



while True:
    conn, addr =s.accept()
    print("Verbunden mit: ", addr)

    start_new_thread(threaded_client,  (conn,))

