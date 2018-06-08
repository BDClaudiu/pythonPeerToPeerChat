import socket

class ClientSocket:

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    print("Enter your name ")
    name = input()
    ipAddress=socket.gethostbyname(socket.gethostname())
    while True:

        print(ipAddress+ " Type")
        message = input()
        parseMessage=" ["+name+"] " + message
        print ("UDP target IP:", UDP_IP)
        print ("UDP target port:", UDP_PORT)
        print ("message:", parseMessage)

        sock = socket.socket(socket.AF_INET, # Internet
                                socket.SOCK_DGRAM) # UDP
        sock.sendto(parseMessage.encode(), (UDP_IP, UDP_PORT))

        if message=="quit":
            break;
