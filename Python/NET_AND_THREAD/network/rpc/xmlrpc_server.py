from xmlrpc.server import SimpleXMLRPCServer

def double(num):
    return num * 2

server = SimpleXMLRPCServer(("localhost", 6789)) # Открываем сервер на определенном сокете.
server.register_function(double, "double") # Регистрируем функцию, чтобы она была доступна клиентам
server.serve_forever()