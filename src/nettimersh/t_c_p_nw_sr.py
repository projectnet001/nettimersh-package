import socket
import threading

SERVER  = socket.gethostbyname(socket.gethostname())
PORT = 5050
#HEADER = 64
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)
USERS = {'oktay': '192.168.1.1', 'john' : '192.168.1.2'}

chat_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chat_server.bind(ADDR)

def handle_client(conn, addr):
    print("[CONNECTED] connected with {}".format(addr))

    connected = True
    while connected:
        #mes_length = conn.recv(HEADER).decode(FORMAT) #receive as string
        message = conn.recv(1024).decode(FORMAT)
        if(message == "kill" or message == "KILL" or message == ""):
            connected = False
            print("[DISCONNECTED FROM {}]".format(addr))
        else:
            print("[MESSAGE FROM {}] {}".format(addr, message))
    
    conn.close()

def start():
    try:
        chat_server.listen(10)
        print("[WAITING] waiting for connections...")
        while 1:
            client, addr = chat_server.accept()
            thread = threading.Thread(target = handle_client, args=(client, addr))
            thread.start()
            #print("[ACTIVE CONNECTIONS] {}".format(threading.active_count()-1))
    except KeyboardInterrupt:
        exit() #doesn't work :(
        
print("[STARTING] server is starting...")
start()

