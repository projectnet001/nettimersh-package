import socket


UDP_IP = "10.33.116.166"
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

while 1:
    MESSAGE = input()
    sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))


