import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # choose UDP protocol
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# specify the socket format
PORT = 1060
network = '140.118.208.232'

s.sendto('Hi, B10702113!!!'.encode('utf-8'), (network, PORT))
data, address = s.recvfrom(65535) # waiting until server connecting
print(data.decode('utf-8'))
s.close()