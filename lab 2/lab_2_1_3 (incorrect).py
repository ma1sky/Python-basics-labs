import random 
with open("ip.log", "w") as ipLogs:
    for i in range(0, 10000):
        random.seed(i)
        print(":".join("{0:04x}".format(ipv6) for ipv6 in [random.randint(0, 29999) for hexNumbers in range(8)]), file=ipLogs)
ipLogs.close()