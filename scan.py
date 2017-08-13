#!/usr/bin/env python

import socket
from socket import *

if __name__ == '__main__':
    pc = raw_input('Ingresa el dominio o IP: ')
    ippc = gethostbyname(pc)
    print 'Iniciando escaneo de ', ippc;

    for ports in range(19, 1000):
        client = socket(AF_INET, SOCK_STREAM)
        result = client.connect_ex((ippc, ports))

        if (result == 0):
            print 'Puerto %d: Abierto' %(ports);
            client.close()