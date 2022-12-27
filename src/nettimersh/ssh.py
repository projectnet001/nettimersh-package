from netmiko import ConnectHandler


ip=input('Enter IP address: ')
username=input('Enter username: ')
password=input('Enter password: ')
port=input('Enter port number: ')

MT = {
    'device_type': 'mikrotik_routeros',
    'host': ip,
    'port': port,
    'username': username,
    'password': password
}

ssh = ConnectHandler(**MT)
print('Connected to {}.'.format(ip))


print("""
Commands:
1. ip route print
2. interface print
3. Other
4. Disconnect
""")

while(True):
    choice=input('Enter command number:')

    if choice=="1":
        output = ssh.send_command('ip route print')
    elif choice=="2":
        output = ssh.send_command('interface print')
    elif choice=="3":
        command=input('Enter custom command: ')
        try:
            output = ssh.send_command(command)
        except Exception as e:
            print('Something went wrong:')
            print(e)
    elif choice=="4":
        break
    else: print('Invalid input!')

    print(output)

