import ipaddress as ip
userIp = ip.IPv6Address(str(input('Ввод ipaddress: ')))

def compareIps(ip1, ip2):
    if ip1 == ip2:
        return f'{ip1} == {ip2}'
    elif ip1 > ip2:
        return f'{ip1} > {ip2}'
    else:
        return f'{ip1} < {ip2}'
    
with open('lab 2/ip.log', 'r') as ipLogs:
    with open('lab 2/ip.solve', 'w') as ipSolve:
        for i in range(10000):
            comIp = ip.IPv6Address(ipLogs.readline().rstrip('\n'))
            print(compareIps(comIp, userIp), file=ipSolve)
    ipSolve.close()
ipLogs.close()