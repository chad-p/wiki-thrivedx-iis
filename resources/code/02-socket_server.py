import socket

mysocket = socket.socket()
mysocket.bind(("127.0.0.1", 50002))
mysocket.listen(2)
conn, addr = mysocket.accept()

buffer = 25
data = b""
#print(conn)
while True:
    packet = conn.recv(buffer)
    #print("packet: ", packet)
    parsed = packet.decode()
    #print("parsed: ", parsed)
    data += packet
    print(parsed, end="---")

    if len(packet) < buffer:
        print("\n------Server Message------\n"
              "All the data has been "
              "received successfully!")
        break

mysocket.close()
