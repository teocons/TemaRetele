import socket
import logging

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 10000
adresa = '0.0.0.0'
server_address = (adresa, port)
sock.bind(server_address)
window_size = 1000
window_left = 1
window_right = window_size
total_package_num = 10000
received = [0] * (total_package_num + 10)
logging.info("Serverul a pornit pe %s si portnul portul %d", adresa, port)
numprim = 0
while window_left <= total_package_num:
      while True:
            window_right = window_left + window_size - 1
            data, address = sock.recvfrom(2048)
            if (int(data) >= window_left and int(data) <= window_right
                and data and received[int(data)] == 0):
                received[int(data)] = 1

            if (data and int(data) <= window_right):
                sock.sendto(data, address)
                logging.info("Am primit " + str(data))
                while(window_left <= total_package_num and
                      received[window_left] == 1):
                      window_left = window_left + 1



