import socket
from _thread import *
from Panzerbwegung import Player
import pickle
import pygame


#ip
server = "192.168.178.96" #192.168.2.108 kf #134.103.111.15
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

#was in den playern drin ist

players = [Player(100,316,0,0,(255,0,0), "Player 1", 1000, True), Player(600, 320, 0,0,(0,0,255), "Player 2", 1000, False)]



def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(8192))
            players[player] = data


            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
