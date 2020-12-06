import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # choose UDP protocol
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# specify the socket format
PORT = 1060
s.bind(('127.0.0.1', PORT))
print('Listening for broadcast at ', s.getsockname())

while True: # wait all the time, and can't shut down
    data, address = s.recvfrom(65535) # waiting until client connecting
    print(data.decode('utf-8')) # need decoding
    s.sendto('Thank you, B10702113~~'.encode('utf-8'), (address))
    print('Receive data from: ',address)