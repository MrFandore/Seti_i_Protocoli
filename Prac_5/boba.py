import netmiko

devices = {
    "SW1": "192.168.92.30",
    "SW2": "192.168.92.31",
    "SW10": "192.168.92.50",
    "SW11": "192.168.92.51",
    "PROVIDER": "192.168.92.70",
    "R1": "192.168.92.10",
    "R10": "192.168.92.20",
}

creds = {
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
}

vlan_to_create = 81
ips = {
    devname: f"192.168.{vlan_to_create}.{i + 100}"
    for i, devname in enumerate(devices.keys())
}

for devname, ip in ips.items():
    dev = creds.copy()
    dev["host"] = devices[devname]

    try:
        ssh = netmiko.ConnectHandler(**dev)
        ssh.enable()
        ssh.send_command_timing('configure terminal')

        if devname[0] != 'R':
            commands = [
                f'vlan {vlan_to_create}',
                f'name vlan{vlan_to_create}',
                f'int vlan{vlan_to_create}',
                f'ip address {ip} 255.255.255.0',
                'no sh',
            ]
        else:
            commands = [
                f'int gi0/1.{vlan_to_create}',
                f'description vlan{vlan_to_create}',
                f'encapsulation dot1Q {vlan_to_create}',
                f'ip address {ip} 255.255.255.0',
                'no cdp enable',
            ]

        print(ssh.send_config_set(commands))
        print(f'Created VLAN {vlan_to_create} for {devname}')

    except Exception as e:
        print(f'Failed to configure device {devname}: {e}')

    finally:
        ssh.disconnect()
