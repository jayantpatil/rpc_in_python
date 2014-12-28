import socket
import client
import sys

def end_program():
    print client.client(sys.argv[1])
    

end_program()
