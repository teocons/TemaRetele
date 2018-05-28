from scapy.all import *
from struct import *
import sys

ip = IP()

ip.src = '198.13.0.15' #mid1
ip.dst = '198.13.0.14' #rt1

#DSCP de AF33 = 011110
dscp = '011110'
ecn = '11'
ip.tos = int(dscp + ecn, 2) # adaugatDSCP si ECN


tcp_obj = TCP()
tcp_obj.sport = 54321
tcp_obj.dport = 5000

option = 'MSS'
optionIndex = TCPOptions[1][option]
optionFormat = TCPOptions[0][optionsIndex]

# Facem segment size-ul de la MSS = 2

valoare = struct.pack(optionFormat[1], 2)
tcp_obj.options = [(option, valoare)]
# EC = ECE + CWR
tcp_obj.flags = 'EC'

tcp_obj.seq = 0 # Fiind primul pachet trimis incepem sequence-ul cu 0
#Puteam incepe si cu un numar random
tcp_obj.flags = 'S' # flagul de sincronizare
raspuns = sr1(ip/tcp_obj) 

tcp_obj.seq += 1
tcp_obj.ack = raspuns.seq + 1
tcp_obj.flags = 'A' #flagul de acknowledge = flagul de sincronizare de la celalalt + 1
ACK = ip / tcp_obj

send(ACK) #trimitem acknowledge

outString = "fin";

for char in outString:

    #PAEC = PSH + ACK + ECE + CWR
    tcp_obj.flags = 'PAEC'
    tcp_obj.ack = raspuns.seq + 1

    #Verificare caracter trimis
    print "Character sent: " + char

    #Trimitere pachet format din ip + tcp + char(caracter)
    rcv = sr1(ip/tcp_obj/char)
    tcp_obj.seq += 1


#RST Flag
tcp_obj.flags='R'
RESET = ip/tcp_obj

#Trimitere Reset
send(RESET)
