import os
import socket
import threading
import random
import rsa
from cryptography.fernet import Fernet

# #creating users
users={}
def adduser():
    print('enter [quit] to quit')
    while True: 
        username=input("Username: ")
        password=input("Password: ")
        
        if(username == 'quit' or password == 'quit'):
            break

        users[username]=password
adduser()
print(users)

#creating prime numbers
primes = [i for i in range(10000, 20000) if rsa.is_prime(i)]
p = random.choice(primes)
primes.remove(p)
q = random.choice(primes)
    
public, private = rsa.generate_key_pair(p, q)
print(public, private)


#socket creation
serverSocket=socket.socket()
ip="127.0.0.1"
port=8888
serverSocket.bind((ip,port))
serverSocket.listen(10)
clients = []
names = []
keys = []


def closeAll(clients):
    for client in clients:
        client.close()


def listen_for_input():
    while True:
        signal = input("")
        if (signal == "exit"):
            closeAll(clients)
            serverSocket.close()
            os._exit(1)
        if (signal == "update"):
            adduser()


def remove(client):
    if client in clients:
        index=clients.index(client)
        clients.remove(client)
        del names[index]
        del keys[index]

def clientThread(address, connection):
    index = clients.index(connection)
    fer = keys[index]
    connection.send(fer.encrypt("Welcome to chatroom".encode()))
    while True:
        try:
            message = fer.decrypt(connection.recv(1024)).decode()
            if message:
                txt = "<"+address[0]+"><"+names[index]+"> "+message
                print(txt)
                broadcast(txt,connection)
            else:
                connection.close()
                remove(connection)
        except:
            connection.close()
            remove(connection)

def broadcast(message,connection):
    for client in clients:
        if (client!=connection):
            try:
                index=clients.index(client)
                fer=keys[index]
                client.send(fer.encrypt(message.encode()))
            except:
                client.close()
                remove(client)

print("To close server enter [exit]")
threadex = threading.Thread(target=listen_for_input)
threadex.start()
while(True):
    clientConnection, clientAddress=serverSocket.accept()
    clientConnection.send(public.encode())
    print("Public key has been sent to client")
    encryptedkey=clientConnection.recv(1024).decode()
    key=rsa.decrypt(private,encryptedkey)
    print("the key for symmetric encryption has been received from client and saved")
    f=Fernet(key)
    i=0
    while (i<3):
        credentials = f.decrypt(clientConnection.recv(1024)).decode()
        username= credentials.split("---")[0]
        password= credentials.split("---")[1]
        if (username in users and users[username]==password):
            clientConnection.send(f.encrypt("yes".encode()))
            break
        else:
            clientConnection.send(f.encrypt("no".encode()))
        i+=1
    
    if (i==3):
        continue
    if (username in names):
        clientConnection.send(f.encrypt("error: there is a user with this username in chatroom".encode()))
        continue

    clients.append(clientConnection)
    keys.append(f)
    names.append(username)
    message = clientAddress[0] + " with this nickname: " + username + " connected to chatroom"
    print(message)
    broadcast(message, clientConnection)
    thread = threading.Thread(target=clientThread,args=(clientAddress, clientConnection))
    thread.start()
