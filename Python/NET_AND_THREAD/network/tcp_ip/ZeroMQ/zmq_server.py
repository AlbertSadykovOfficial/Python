import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context() # Создаем ZeroMQ объект
server = context.socket(zmq.REP) # REP - синхронный ответ
server.bind("tcp://%s:%s" % (host, port)) # Заставляем слушать адрес и порт
while True:
    #  Wait for next request from client
    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')
    print("That voice in my head says: %s" % request_str)
    reply_str = "Stop saying: %s" % request_str
    reply_bytes = bytes(reply_str, 'utf-8')
    server.send(reply_bytes)