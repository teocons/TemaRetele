#python /elocal/rezolvare\ tema2/tcpmodif.py

import sys
import socket
import logging
import time

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = '0.0.0.0'
port = 5000

server_address = (address, port)
sock.bind(server_address)
logging.info("Server started " + str(adress) + ":" + str(port))

logging.info('Waiting for connection')
sock.listen(1)

conn, address = sock.accept()
logging.info("Handshake with " + str(address))

while True:
    info = conn.recv(1)
    logging.info('Received : ' + str(info))
    info = chr(ord(str(info)[0]) - 5)
    conn.send(info)
    logging.info('Sent : ' + str(info))

conn.close()
sock.close()
