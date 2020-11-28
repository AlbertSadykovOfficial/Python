import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 1000

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM - установ тиь протокл TCP
client.connect(address) # Устанавливаем соединение (в отличие от UDP, где мы просто отсылаем)
client.sendall(b'Hey!')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()