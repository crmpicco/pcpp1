import socket
def printServiceOnPort(portNumber, protocol):
    #input missing code
    serviceName = socket.getservbyport(portNumber, protocol)

    print("Name of the service running at port number %d : %s"%(portNumber, serviceName))

printServiceOnPort(80,  "tcp")
