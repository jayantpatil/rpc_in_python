import socket
#import sys


#inp = sys.argv[1].split(",")
#print inp
def client(inp):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("localhost",5000))
    s.send(inp)
    return s.recv(1024)


#client()

