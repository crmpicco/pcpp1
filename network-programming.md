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
