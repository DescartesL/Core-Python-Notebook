from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message ...')
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    response = '[%s] %s' % (ctime(), data.decode('utf-8'))
    udpSerSock.sendto(response.encode('utf-8'),addr)
    print('..received from and returned to:')

udpSerSock.close()