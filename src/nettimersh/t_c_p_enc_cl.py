import os
import socket
import threading
import rsa
from cryptography.fernet import Fernet


#create socket
socketObject=socket.socket()
ip="127.0.0.1"
port=8888
socketObject.connect((ip,port))
print("Connected to {} to port {}".format(ip,port))


key = Fernet.generate_key()
f=Fernet(key)
public=socketObject.recv(1024).decode()
print("This is the public key of server: ",public)
print("This is the key for symmetric encryption: ",key)
encryptedkey = rsa.encrypt(public,key)
socketObject.send(encryptedkey.encode())
print("the key encrypted with server's public key and sent to server")
i=0

while (i<3):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    credentials = username + "---" + password
    socketObject.send(f.encrypt(credentials.encode()))
    response = f.decrypt(socketObject.recv(1024)).decode()
    if (response == "yes"):
        break
    else:
        print("You entered wrong credentials")
    i+=1
if (i==3):
    print("This was your last chance")
    socketObject.close()
    os._exit(1)

txt=f.decrypt(socketObject.recv(1024)).decode()
if (txt.startswith("error:")):
    print(txt)
    os._exit(1)

print(txt)
print("If you want to exit just enter exit")


def listening():
    while True:
        try:
            message = f.decrypt(socketObject.recv(1024)).decode()
            print(message)
        except:
            socketObject.close()
            os._exit(1)

def sending():
    while True:
        try:
            mytext = input("")
            if (mytext=="exit"):
                socketObject.close()
                os._exit(1)
            socketObject.send(f.encrypt(mytext.encode()))
        except:
            continue

thread1 = threading.Thread(target=listening)
thread2 = threading.Thread(target=sending)
thread1.start()
thread2.start()