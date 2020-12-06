import socket
HOST = '140.118.208.95' # the IP address of server
PORT = 7777 # the port of server (not default service port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create a socket object to receive text
# socket.AF_INET: IPv4 (Default) transmission between different devices
# socket.SOCK_STREAM: TCP (Default)
server.bind((HOST, PORT)) # bind the address to the socket object
server.listen(10) # specific the limit number of clients

while True: # always running
    conn, addr = server.accept() # wait for client connecting
    print("conn: ",conn)
    # all information of client is in 'conn'
    # proto: kind of protocol, default is 0 
    print("addr: ",addr)
    clientMessage = str(conn.recv(1024), encoding='utf-8')

    print('Client message is:', clientMessage)

    serverMessage = 'Thank you, B10702113'
    conn.sendall(serverMessage.encode()) # complete encoding, and send all of data (not specific length)
    conn.close()