import socket

def close_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)

    s.connect(server_address)

    message = "Hello, server!"
    s.sendall(message.encode())

    data = s.recv(1024)
    print("Received:", data.decode())
    # insert line of code here
    s.close()

close_connection()
