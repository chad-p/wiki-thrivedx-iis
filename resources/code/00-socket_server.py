import socket  # https://docs.python.org/3/library/socket.html

new_socket = socket.socket()
new_socket.bind(("127.0.0.1", 50000))
new_socket.listen(4)  # number of queued connections that the system will allow before refusing new connections.

conn, addr = new_socket.accept()

print(conn)
print(addr)

new_socket.close()