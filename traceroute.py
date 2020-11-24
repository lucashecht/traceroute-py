import sys
from scapy.all import *

def check_hops(dst, verbose=False):
    p = IP(dst=dst, ttl=1)/ICMP()
    while(True):
        answ = sr1(p, verbose=0)
        if verbose:
            print(f"{p.ttl}: {answ.src}")
        if answ.src == dst:
            return p.ttl
        else:
            p.ttl += 1

if __name__ == '__main__':
    hops = check_hops(sys.argv[1], verbose=True)
    print(f"{hops} hops")
