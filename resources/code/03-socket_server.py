import socket

try:
    mysocket = socket.socket()
    mysocket.bind(('127.0.0.1', 50003))
    mysocket.listen(1)
    print("waiting for connection...")
    c, addr = mysocket.accept()
    print("client connection details are -> {}".format(addr))

    while True:
        sendData = input("message to client : ")
        c.send(sendData.encode())

        if sendData == "exit":
            c.close()
            break

        rcvData = c.recv(1024).decode()
        print("message from client : {}".format(rcvData))

        if rcvData == "exit":
            print("connection as closed by user".encode())
            c.close()
            break

except Exception as e:
    print(e)
