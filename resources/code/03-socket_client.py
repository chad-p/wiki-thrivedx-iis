import socket

try:
    mysocket = socket.socket()
    mysocket.connect(('127.0.0.1', 50003))
    print("connection established...")

    while True:
        serverData = mysocket.recv(2048).decode()
        print("message from server : {}".format(serverData))

        if serverData == "exit":
            print("connection as closed by server")
            mysocket.close()
            break

        sendData = input("message to server : ")
        mysocket.send(sendData.encode())

        if sendData == "exit":
            print("connection as closed by client")
            mysocket.close()
            break

except Exception as e:
    print(e)
