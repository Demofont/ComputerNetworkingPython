import socket
 
HOST = "127.0.0.1"
PORT = 50007
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # cf. tcpserver.py
print('Socket created')
 
s.connect((HOST,PORT))
print('Connected to', HOST, ':', PORT)
 
data = ""       # Initialize data
 
while(data != 'q'):
        msg = input("Say: ")
        s.sendall(msg.encode())
        data = s.recv(1024).decode()
        print('Echo:', repr(data))
 
s.close()
print('Connection closed')