from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 1000 # Максимально число байтов, которое принимаем от клиента

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)  	# Максимальное кол-во клиентских соединений, будет выдавать отказ послежующим клиентам 

client, addr = server.accept()
data = client.recv(max_size) # Установка значения Max кол-ва байтов

print('At', datetime.now(), client, 'said', data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()