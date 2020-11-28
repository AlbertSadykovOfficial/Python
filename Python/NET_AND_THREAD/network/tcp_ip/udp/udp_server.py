from datetime import datetime
import socket

server_address = ('localhost', 6789) # Определяем сокет 
max_size = 4096

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')

# Создаем сокет (AF_INET-интернет (ip) сокет, SOCK_DGRAM- будем отправлять и получать датаграммы, т.е. UDP)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address) # Привязываем к сокету адрес.

data, client = server.recvfrom(max_size) # Ждем прихода датаграм, когда они появятся, сервер проснется

print('At', datetime.now(), client, 'said', data)
server.sendto(b'Are you talking to me?', client)
server.close()