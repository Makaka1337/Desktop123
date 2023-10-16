from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)



udpCliSock = socket(AF_INET, SOCK_DGRAM)
while True:


    message = input('Введите сообщение: ')
    udpCliSock.sendto(message.encode('utf-8'), ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZE)
    print('Получено сообщение:', data.decode('utf-8'), 'от', addr)

    udpCliSock.close()