import socket

HOST = '192.168.43.57' # the IP address of destination
PORT = 7777 # the port of destination
clientMessage = 'hi, B10702113'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# build the socket object to transmit text
# socket.AF_INET: IPv4 (Default)
# socket.SOCK_STREAM: TCP (Default)
client.connect((HOST, PORT)) # connection
client.sendall(clientMessage.encode())

serverMessage = str(client.recv(1024), encoding='utf-8')
# specific the message from the server(the message limit is 1k)
print('server response:', serverMessage)

client.close() # close the object