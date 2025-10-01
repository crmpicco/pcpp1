import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('www.procoding.rs', 80)
client_socket.connect(server_address)

request = "GET / HTTP/1.1\r\nHost: www.procoding.rs\r\n\r\n"
client_socket.send(request.encode())

response = client_socket.recv(4096)

print(response.decode())

client_socket.close()
