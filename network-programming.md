# Network Programming

## JSON
To parse a JSON string into a Python object, use the `json.loads()` method from the `json` module.
```python
import json
customer_info = '{"name": "Craig", "age": 41, "city": "Rockingham"}'
customer = json.loads(customer_info)
```

To convert Python data types into JSON data, use the `json.dumps()` method.
```python
import json
club = {"club": "Rangers", "year_founded": 1872, "city": "Glasgow"}
club_info = json.dumps(club)
```

## socket
The `socket` module provides access to the BSD socket interface. It is used to create network connections and communicate over the network.

`socket.accept()` - allows a server socket to accept requests from a client socket from another host.
```python
import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_socket.bind(('0.0.0.0', 8080))

# start listening for incoming connections (max 5 clients in the queue)
server_socket.listen(5)

while True:
    # accept an incoming connection
    client_socket, client_address = server_socket.accept()    
    client_socket.sendall(b"Hello! You are connected.\n")
    client_socket.close()
```

`socket.connect()` - used to connect a socket to a remote address. You need to pass the address and port of the server you want to connect to **as a tuple**.

`socket.recv()` - used to receive data from a socket. It is commonly used in client-server applications to receive data from a server. It takes one argument which specifies the maximum number of bytes to receive in a single call.
```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8443)
client_socket.connect(server_address)

# send a message to the server
message = 'Ahoy hoy, server!'
client_socket.sendall(message.encode('utf-8'))

# receive data from the server (up to 1024 bytes, you can change this value to receive more bytes in a single call)
data = client_socket.recv(1024)
print('Received from server:', data.decode('utf-8'))
```
`socket.getservbyport()` - used to get the service name associated with a port number. It takes two arguments: the port number and the protocol name (e.g. `tcp` or `udp`).
```python
import socket

service = socket.getservbyport(80, 'tcp')
print(f"Service on TCP port 80: {service}")
# http

service = socket.getservbyport(53, 'udp')
print(f"Service on UDP port 53: {service}")
# domain
```
## General

### IP (Internet Protocol)
- One of the lowest layers of the TCP/IP model
- Doesn't guarantee that any of the sent datagrams/packets will reach the target
- Doesn't guarantee that the datagrams/packets will be received in the same order they were sent
- Doesn't guarantee that the datagrams/packets will be received at all or reach the target intact