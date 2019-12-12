import socket
import decryptor
import dbc

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8159
print (host)
print (port)
serversocket.bind((host, port))

serversocket.listen(5)
print ('server started and listening')
while 1:
    (clientsocket, address) = serversocket.accept()
    print ("connection found!", address)
    data = clientsocket.recv(1024)
    data = decryptor.decryptor(data)
    dbc.pwcheck(data)
    print("data rcvd:", data)
    r='message recieved'
    clientsocket.send(r.encode())
