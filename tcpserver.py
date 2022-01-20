import socket
 
HOST = "127.0.0.1"      # localhost
PORT = 50007            # random port
echolog = []
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket
print('Socket created')                         # with adress family AF_INET
                                                # & type SOCK_STREAM (TCP)
s.bind((HOST, PORT))    # Bind socket with a tuple host and port numbers
print('Socket bound')
 
s.listen(5)
print('Listening for connections...')
 
conn, addr = s.accept()
print('Connected by', addr)
 
while True:
        data = conn.recv(1024)  # Receive Data
        conn.sendall(data)      # Send it right back
        data = data.decode()    # Decode the byte representation to a string
        print('Echoed: ', data) # Print it to the console
        echolog.append(data)    # Add it to the log list
        if data.lower()=='q': break     # End connection if client enters q
conn.close()
 
print('Connection closed, following strings have been echoed', echolog)
