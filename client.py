import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = "18.222.230.166"
#port = 8159
#s.connect(("18.222.230.166",8159))

def ts(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "18.191.117.109"
    port = 8159
    s.connect(("18.191.117.109", 8159))
    s.send(data)
    data = ''
    data = s.recv(1024).decode()
    print (data)
