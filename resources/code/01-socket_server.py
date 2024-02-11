import socket

new_socket = socket.socket()
new_socket.bind(("127.0.0.1", 50001))
new_socket.listen()
conn, addr = new_socket.accept()

data = conn.recv(2048).decode()
print(data)

new_socket.close()
