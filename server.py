import socket
HOST = 'localhost' # Server IP address
PORT = 12345 # Server port number
def receive_file():
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
 server_socket.bind((HOST, PORT))
 server_socket.listen(1)
 print('Waiting for connection...')
 client_socket, addr = server_socket.accept()
 print('Connected to:', addr)
 with open('received_file', 'wb') as file:
 while True:
 data = client_socket.recv(1024)
 if not data:
 break
 file.write(data)

 print('File received successfully.')
receive_file()