import socket
def printServiceOnPort(portNumber, protocol):

    serviceName = socket.getservbyport(portNumber, protocol)

    print("Name of the service running at port number %d : %s"%(portNumber, serviceName))

printServiceOnPort(80,  "tcp")
printServiceOnPort(21,  "tcp")
printServiceOnPort(53,  "tcp")
