import sys
from scapy.all import srp, Ether, ARP, conf

eth = Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = '198.13.13.0/16')
answ, unansw = srp(eth / arp, timeout = 10)
for snd, rcv, in answ:
    print rcv.sprintf(r"%Ether.src% - %ARP.psrc%")
