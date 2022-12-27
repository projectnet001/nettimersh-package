import socket

c = socket.socket()
host = socket.gethostname()

c.connect((host,5050))

while True: 
    msg = input("message: ")
    c.send(bytes(msg, "utf-8"))
