import nmap
import threading

nmScan = nmap.PortScanner()
nmScan.scan(hosts='192.168.181.0/24', arguments='-sS -T4')

def scan_port(host, port, details):
    state = details['state']
    name = details.get('name', 'unknown')
    print(f" Port {port} ({name}): {state}")
    if state == 'open':
        print(f" >>> Port {port} is open and can be used by intruders.")

def callback_result(host, scan_result):
    print('------------------')
    print(host, scan_result)

threads = []
for host in nmScan.all_hosts():
    if 'tcp' in nmScan[host]:
        ports = nmScan[host]['tcp']
        print('----------------------------------------------------')
        print(f'Host : {host} ({nmScan[host].hostname()})')
        print(f'State : {nmScan[host].state()}')
        for port, details in ports.items():
            # Создаем поток для обработки каждого порта
            thread = threading.Thread(target=scan_port, args=(host, port, details))
            threads.append(thread)
            thread.start()

for thread in threads:
    thread.join()
