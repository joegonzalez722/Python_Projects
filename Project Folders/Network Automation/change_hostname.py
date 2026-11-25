from netmiko import ConnectHandler

SWITCH = {
    'device_type': 'cisco_ios',
    'host': '192.168.99.1',
    'username': 'admin',
    'password': 'Pa$$w0rd'
}

net_connect = ConnectHandler(**SWITCH)
print(f'Connected to {SWITCH["host"]}')

hostname = input("Enter the new hostname for the switch: ")

net_connect.send_command([f'hostname {hostname}'])

print(net_connect.send_command('show run | include hostname'))

net_connect.save_config()
net_connect.disconnect()
print('configuration saved and connection closed')


