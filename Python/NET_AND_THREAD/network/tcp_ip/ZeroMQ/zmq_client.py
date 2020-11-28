import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context() # Создаем ZeroMQ объект
client = context.socket(zmq.REQ) # REP - синхронный запрос
client.connect("tcp://%s:%s" % (host, port)) # Подключаемся по сокету: адрес и порт
for num in range(1, 6):
    request_str = "message #%s" % num 
    request_bytes = request_str.encode('utf-8') # Преобразовать в байтовую строку
    client.send(request_bytes)
    reply_bytes = client.recv()
    reply_str = reply_bytes.decode('utf-8')
    print("Sent %s, received %s" % (request_str, reply_str))