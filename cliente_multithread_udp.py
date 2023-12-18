import socket
import threading

def receber_mensagens(sock):
        data = sock.recv(2048)
        mensagem = data.decode()
        #Imprimindo a mensagem recebida
        print(data.decode())

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
server_address = ('localhost', 20001)
print ("Conectando %s porta %s" % server_address)
#Conectando ao servidor
sock.connect(server_address)
recepcao = threading.Thread(target=receber_mensagens,args=(sock,))
recepcao.start() 

message = input("Solicite o horário: ")
#Enviando mensagem ao servidor
sock.sendall(message.encode('utf-8'))

recepcao.join()