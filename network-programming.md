# Network Programming

## JSON
### loads
To parse a JSON string into a Python object, use the `json.loads()` method from the `json` module.
```python
import json
customer_info = '{"name": "Craig", "age": 41, "city": "Rockingham"}'
customer = json.loads(customer_info)
```
### dumps
To convert Python data types into JSON data, use the `json.dumps()` method.
```python
import json
club = {"club": "Rangers", "year_founded": 1872, "city": "Glasgow"}
club_info = json.dumps(club)
```
You can't dump the content of an object by default, as the `json` module doesn't know how to convert it to JSON. You need to define a custom method to convert the object to a dictionary or use the `default` parameter of `json.dumps()` to specify a function that converts the object to a JSON-serializable format.
```python
import json

class Competition:
    def __init__(self, name, prize_money):
        self.name = name
        self.prize_money = prize_money

def encode_competition(competition):
    if isinstance(competition, Competition):
        return competition.__dict__
    
    raise TypeError(f"Object of type {competition.__class__.__name__} is not JSON serializable")

the_open = Competition("The Open Championship", 1860)
print(json.dumps(the_open, default=encode_competition))
# {"name": "The Open Championship", "prize_money": 1860}
```    

Python objects [converted to their JSON equivalents](https://docs.python.org/3/library/json.html#json.JSONEncoder):

| Python  | JSON                 | 
|---------|----------------------|
| `int`   | Number               |
| `float` | Number               |
| `list`  | Array                |
| `dict`  | Object               |
| `tuple` | Array                |
| `list`  | Array                |
| `str`   | String               |
| `True`  | true                 |
| `False` | false                |
| `None`  | null                 |
| `set`   | :x: Incompatible :x: |

```python
import json

f1_data = {
    "laps": 58,                 
    "circuit": "Monza",         
    "safety_car": True,         
    "red_flag": False           
}

json_output = json.dumps(f1_data, indent=2)
print(json_output)
#{
#  "laps": 58,
#  "circuit": "Monza",
#  "safety_car": true,
#  "red_flag": false
#}
```

## socket
The `socket` module provides access to the BSD socket interface. It is used to create network connections and communicate over the network.

`socket.accept()` - allows a server socket to accept requests from a client socket from another host.
```python
import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
# the domain is typically not part of a socket itself, but rather it is used to resolve the IP address that the socket connects to
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

`socket.recv()` - used to receive data from a socket. It is commonly used in client-server applications to receive data from a server. It takes one argument which specifies the maximum number of bytes to receive in a single call. It will wait/block until it receives **at least one byte** or until a timeout or an error occurs. The return value of this method is a bytes object representing the data received.
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
Clients - request services from servers. They initiate the connection to the server and send requests for data or services.

Servers - provide services to clients. They listen for incoming connections and respond to client requests.

## XML
The `xml.etree.ElementTree` module provides a simple and efficient way to parse and create XML documents. It is part of Python's standard library.

`Element()` - used to create a new XML element.

`SubElement()` - used to create a new sub-element under an existing element.

`attrib` - a dictionary that contains the attributes of an XML element.

`find()` - used to find a sub-element with a specific tag

`findall()` - used to find all sub-elements with a specific tag

```python
import xml.etree.ElementTree as ET

event_element = ET.Element('event')
print(type(event_element.attrib))
# prints # <class 'dict'>
```
`parse()` - used to parse an XML document from a string or a file. It returns an `ElementTree` object that represents the entire XML document.

The following code parses an XML file and changes the tag of each child element to `football_competition`:
```python
import xml.etree.ElementTree as ET
competitions = ET. parse('competitions.xml')
root = competitions.getroot()
for child in root:
    child.tag = 'football_competition'
```
Sample XML file (`competitions.xml`):
```xml
<?xml version="1.0"?>
<competitions>
    <competition name="Scottish Cup">
        <author>Scottish Football Association</author>
        <year>1873</year>
    </competition>
    <competition name="Scottish League Cup">
        <author>Scottish Professional Football League</author>
        <year>1946</year>
    </competition>
</competitions>
```

### DTD
**D**ocument **T**ype **D**efinition. It defines the structure and the legal elements and attributes of an XML document. It is used to validate the XML document against a set of rules.

You can use internal or external DTD declarations.

From a DTD point of view, all XML documents are made up of several building blocks:
* Elements
* Attributes
* Entities
* PCDATA (Parsed Character Data)
* CDATA (Character Data)

## [requests](https://requests.readthedocs.io/en/latest/)
The `requests` module is a popular Python library for making HTTP requests. It provides a simple and intuitive API for sending HTTP requests and handling responses.

`requests.Session()` - used to manage logins and persist cookies
```python
import requests

session = requests.Session()

login_payload = {
    'username': 'johndoe1872',
    'password': 'p4ssw0rd123'
}
session.post('https://example.com/login', data=login_payload)

# then use the session to access protected pages that require authentication
response = session.get('https://example.com/protected-page')
print(response.text)
```
HTTP response headers can be taken from the `headers` attribute of the response object. The headers are returned as a dictionary-like object.
```python
import requests
response = requests.get('https://api.example.com/data')
print(response.headers)
# {'Content-Type': 'application/json', 'Content-Length': '1234', ...}
```
| Header Name    | Description                                                              |
|----------------|--------------------------------------------------------------------------|
| Content-Type   | Describes the media type of the response body (e.g., `application/json`) |
| Content-Length | Size of the response body in bytes                                       |
| Server         | Indicates the software used by the origin server, e.g. `nginx`           |
| Date           | Timestamp when the response was generated by the server                  |
| Set-Cookie     | Sends cookies from the server to the client                              |
## General

### IP (Internet Protocol)
- One of the lowest layers of the TCP/IP model
- Doesn't guarantee that any of the sent datagrams/packets will reach the target
- Doesn't guarantee that the datagrams/packets will be received in the same order they were sent
- Doesn't guarantee that the datagrams/packets will be received at all or reach the target intact

### multiprocessing
This is the only way to achieve true parallelism in Python.

The `multiprocessing` module bypasses the Global Interpreter Lock (GIL) by using separate memory spaces and processes. Each process has its own Python interpreter and memory space, allowing multiple processes to run simultaneously on different CPU cores achieving **true parallelism**.

`threading` vs `multiprocessing`:

`threading` is for I/O-bound concurrency

`multiprocessing` is for CPU-bound parallelism

`queue.Queue` is thread-safe, meaning that multiple threads can safely add and remove items from the queue without causing data corruption or inconsistencies. Specifically designed for thread-safe communication. Safe to use across processes. However, the order in which items arrive is not guaranteed because the processes run in parallel.

#### Global Interpreter Lock (GIL)
The GIL is a mutex/lock used by CPython (the standard implementation of Python) to protect access to Python objects, preventing multiple threads from executing Python bytecodes at once. This means that even in a multithreaded program, only one thread can execute Python code at a time.