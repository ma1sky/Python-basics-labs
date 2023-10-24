import random as r
import ipaddress as ip

with open('lab 2/ip.log', 'w') as ipLogs:
    for i in range(10000):
        r.seed(i)
        print(ip.IPv6Address(r.randint(2**32+1, 2**128)).compressed, file=ipLogs)
ipLogs.close()