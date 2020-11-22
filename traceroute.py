from scapy.all import *

def check_hops(dst):
    p = IP(dst=dst, ttl=1)/ICMP()
    while(True):
        answ = sr1(p)
        if answ.src == dst:
            return p.ttl
        else:
            p.ttl += 1
