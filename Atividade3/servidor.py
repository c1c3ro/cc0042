from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

# Registrar caminho para o servidor
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('10.0.84.198', 21212), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Definição de funções
    mensagens = []

    def armazenar(mensagem):
        mensagens.append(mensagem)
        return True

    def getMensagens():
        return mensagens

    def getServerIP():
        return server.server_address[0]

    def getServerDateTime():
        now = datetime.now()
        formatted_date_time = now.strftime("%Y-%m-%d %H:%M")
        return formatted_date_time

    def clearMessages():
        mensagens.clear()
        return True

    # Registrar funções
    server.register_function(armazenar, 'armazenar')
    server.register_function(getMensagens, 'getMensagens')
    server.register_function(getServerIP, 'getServerIP')
    server.register_function(getServerDateTime, 'getServerDateTime')
    server.register_function(clearMessages, 'clearMessages')

    # Iniciar servidor
    server.serve_forever()
