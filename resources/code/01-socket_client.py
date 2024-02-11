import socket

new_socket = socket.socket()
new_socket.connect(("127.0.0.1", 50001))

data = input("What do you want to send?\n")
new_socket.send(data.encode())

new_socket.close()
