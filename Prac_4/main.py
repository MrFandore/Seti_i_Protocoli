import netmiko

devices = {
    "R1": {
        'device_type': 'cisco_ios',
        'host': '192.168.181.10',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
    },
    "R10": {
        'device_type': 'cisco_ios',
        'host': '192.168.181.20',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
    },
    "SW1": {
        'device_type': 'cisco_ios',
        'host': '192.168.181.30',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
    },
    "SW2": {
        'device_type': 'cisco_ios',
        'host': '192.168.181.31',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
    },
    "SW10": {
        'device_type': 'cisco_ios',
        'host': '192.168.181.50',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
    },
    "SW11": {
        'device_type': 'cisco_ios',
        'host': '192.168.181.51',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
    },
    "PROVIDER": {
        'device_type': 'cisco_ios',
        'host': '192.168.181.70',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
    }
}
for devname, data in devices.items():
    print('Get config from', devname)

device = netmiko.ConnectHandler(**data)
device.enable()

conf = device.send_command('show running-config', read_timeout=60)
with open('cfgs/' + devname + '_cfg' + '.txt', 'w') as f:
    f.write(conf)
