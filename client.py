import socket
HOST = 'localhost' # Server IP address
PORT = 12345 # Server port number
FILE_PATH = 'file_to_send.txt' # Path of the file to be sent
def send_file():
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
client_socket.connect((HOST, PORT))
with open(FILE_PATH, 'rb') as file:
for data in file:
client_socket.sendall(data)
print('File sent successfully.')
send_file()