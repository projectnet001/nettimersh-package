import socket

s = socket.socket()

print("Socket created...")

host = socket.gethostname()
s.bind((host, 5000))

s.listen(3)
print("waiting for connections...")


c, address = s.accept()
while True:
    name = c.recv(1024).decode()
    print("connected with: ", address, " name: ", name)

    c.send(bytes("Welcome to my first ever server!", "utf-8"))
    
c.close()

