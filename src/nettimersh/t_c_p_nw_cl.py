import socket

SERVER  = "10.33.116.166"
PORT = 5050
#HEADER = 64
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)
USERNAME = "oktay"

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.connect(ADDR)

def send():
    connected = True
    while connected:
        receiver_username = input("enter receiver username: ") #john
        sender.send(bytes(receiver_username, FORMAT))
        
        #message = input("=>: ")
        
    sender.close()

send()