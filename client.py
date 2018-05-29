import socket
import logging
import sys

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 10000
adresa = '172.111.0.14'
server_address = (adresa, port)
mesaj = sys.argv[0]
numconfirm = 0
numno = 0
numtrim = 0
window_size = 1000
window_left = 1
total_package_num = 10000
confirmed = [0] * (total_package_num + 10) 
window_right = window_size
sock.settimeout(0.1)

while window_left <= total_package_num:
      for i in range(window_left, min(window_left + window_size, total_package_num + 1)):
          if (confirmed[i] == 0):
              mesaj = str(i)
              logging.info('Trimitem mesajul "%s" catre %s', mesaj, adresa)
              sent = sock.sendto(mesaj, server_address)
              numtrim = numtrim + 1

      logging.info("Mijloc\n")

      while True:
            try:
                data, server = sock.recvfrom(2048)
                logging.info('Content primit: "%s"', data)
                
                if (confirmed[int(data)] == 0):
                    confirmed[int(data)] = 1
                    numconfirm = numconfirm + 1 
            except socket.error:
                logging.info('Confirmation not received')
                numno = numno + 1
                break

      while (window_left <= total_package_num and confirmed[window_left] == 1):
             window_left = window_left + 1

logging.info('Trimise :' + str(numtrim) + ' Confirmate :' + str(numconfirm)+ '\n')
sock.close()
