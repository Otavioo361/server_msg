from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Cria a classe do servidor
class ChatServer:
    def __init__(self):
        self.messages = []

    # Adiciona uma mensagem à lista
    def add_message(self, message):
        self.messages.append(message)
        return True

    # Retorna a lista de mensagens
    def get_messages(self):
        return self.messages

if __name__ == '__main__':
    # Cria o servidor na porta 8000
    with SimpleXMLRPCServer(('localhost', 8000), logRequests=True, allow_none=True) as server:
        # Registra a classe do servidor como um objeto RPC
        server.register_instance(ChatServer())

        print("Servidor iniciado. Aguardando conexões...")
        # Inicia o loop do servidor
        server.serve_forever()
'''A classe ChatServer contém os métodos que podem ser chamados remotamente pelos clientes. Nesse caso, temos os métodos add_message para adicionar uma mensagem à lista e get_messages para obter a lista de mensagens.

Na função principal, é criado o servidor na porta 8000 e a classe ChatServer é registrada como um objeto RPC. O servidor é iniciado e fica aguardando conexões.'''