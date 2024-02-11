import socket

new_socket = socket.socket()

try:
    new_socket.connect(("127.0.0.1", 50000))
except:
    print("The connection was refused")

new_socket.close()