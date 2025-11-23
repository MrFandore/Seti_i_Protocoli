import netmiko
import ipaddress

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.181.20',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
}

cisco_switch = {
    'device_type': 'cisco_ios',
    'host': '192.168.181.30',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
}

commands = [
    'vlan 4',
    'name vlan4',
    'ip 192.168.144.2 255.255.255.0',
]

print('---------------- Router-----------------')
# Настройка подключения роутерa по SSH
ssh_router = netmiko.ConnectHandler(**cisco_router)
# Переход в режим enable:
ssh_router.enable()
print('---------------- Router running-config -----------------')
# Получение текущей конфигурации оборудования
print(ssh_router.send_command('show running-config'))

print('---------------- Router interfaces -----------------')
# Получение информации об интерфейсах оборудования
print(ssh_router.send_command('show interfaces'))

print('---------------- Switch -----------------')
# Настройка подключения коммутаторa по SSH
ssh_switch = netmiko.ConnectHandler(**cisco_switch)
# Переход в режим enable:
ssh_switch.enable()
print('---------------- Switch running-config -----------------')
# Получение текущей конфигурации оборудования
print(ssh_switch.send_command('show running-config'))

print('---------------- Switch interfaces ----------------')
# Получение информации об интерфейсах оборудования
print(ssh_switch.send_command('show interfaces'))

print('---------------- Switch vlan ----------------')
# Получение информации о вланах
print(ssh_switch.send_command('show vlan'))
# Конфигурационный режим
ssh_switch.send_command_timing('configure terminal')
# Удаление vlan4 на коммутаторе
ssh_switch.send_command_timing('no vlan 4')
print(ssh_switch.send_command_timing('end'))

print('---------------- Switch vlan ----------------')
# Получение информации о вланах
print(ssh_switch.send_command('show vlan'))
# Создание vlan4
ssh_switch.send_config_set(commands)
print('---------------- Switch vlan ----------------')
# Получение информации о вланах
print(ssh_switch.send_command('show vlan'))

print('---------------- Switch ARP -----------------')
# ARP
print(ssh_switch.send_command('show arp'))

print('---------------- Switch mac address-table -----------------')
# mac address-table
print(ssh_switch.send_command('show mac address-table'))



# Для ответов на вопросы:
# commands = [
#     'vlan 4',
#     'name vlan4',
#     'ip 192.168.144.2 255.255.255.0',
# ]

# ssh_switch.send_config_set(commands)