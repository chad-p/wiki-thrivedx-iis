'''
Run this after L2 lab and with netcat as server
'''

import socket

new_socket = socket.socket()

try:
    new_socket.connect(("127.0.0.1", 50100))
except:
    print("The connection was refused")

# Send Data
new_socket.send("Hello form the other side\n".encode())

new_socket.close()