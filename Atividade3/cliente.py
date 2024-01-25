#Importar biblioteca
import xmlrpc.client
import socket
#Definir servidor
s = xmlrpc.client.ServerProxy('http://10.0.84.198:21212')

#Chamar funções disponíveis no servidor
s.armazenar("Mensagem!")
print(s.getMensagens())
print(s.getServerIP())
print(s.getServerDateTime())

# Print list of available methods
print(s.system.listMethods())