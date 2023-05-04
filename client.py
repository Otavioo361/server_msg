import xmlrpc.client

# Endereço IP e porta do servidor
SERVER_ADDRESS = 'http://localhost:8000'

# Cria o proxy para o servidor
server_proxy = xmlrpc.client.ServerProxy(SERVER_ADDRESS)

# Loop principal para enviar e receber mensagens
while True:
    # Pede ao usuário para digitar uma mensagem
    message = input("Digite sua mensagem: ")

    # Adiciona a mensagem ao servidor
    server_proxy.add_message(message)

    # Obtém a lista de mensagens do servidor
    messages = server_proxy.get_messages()

    # Exibe a lista de mensagens na tela
    print("Mensagens:")
    for message in messages:
        print("- " + message)
'''Na variável SERVER_ADDRESS, é definido o endereço IP e porta do servidor.

É criado o proxy para o servidor utilizando a biblioteca xmlrpc.client.

Em um loop infinito, o cliente pede ao usuário para digitar uma mensagem e a envia ao servidor utilizando o método add_message do proxy.

Em seguida, o cliente obtém a lista de mensagens do servidor utilizando o método get_messages do proxy.

A lista de mensagens é exibida na tela.'''