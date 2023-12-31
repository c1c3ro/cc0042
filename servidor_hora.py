import socket
import threading
import datetime

def conexao_cliente(client, address):
    
    while (True):    
        data = client.recv(2048)
        '''
        PROTOCOLO
        '''
        mensagem = data.decode()
        if (mensagem!='0'):
            hora = datetime.datetime.now()
            hora = hora.strftime("%H:%M")
            hora = "\nA hora é {}\n".format(hora)
            client.sendall(hora.encode())
        else:
            client.sendall('0'.encode())
            break
    #Fechando o socket
    client.close()

sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  UDP
    
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 20001)
print ("Iniciando servidor na porta %s %s" % server_address)
#Reservando porta
sock.bind(server_address)
#Escutando na porta reservada
sock.listen(1)

#Iniciando protocolo

while True:
    client, address = sock.accept()
    conexao = threading.Thread(target=conexao_cliente,args=(client,address,))
    conexao.start()

