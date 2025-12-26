import sys
import nmap

if len(sys.argv) != 2:
    print("Should be only one argument (e.g. 192.168.92.0/24)")
    exit()

network = sys.argv[1]

nm = nmap.PortScanner()
nm.scan(hosts=network, arguments='-n -sP -PE')

hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

print("Used addresses:")
for host, _ in hosts_list:
    print(f'{host}')
