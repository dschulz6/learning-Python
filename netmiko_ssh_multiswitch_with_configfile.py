from netmiko import ConnectHandler

iosv_l2_s1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.200',
	'username': 'Qwest',
	'password': 'ilfnb980'
}

iosv_l2_s2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.201',
	'username': 'Qwest',
	'password': 'ilfnb980'
}

iosv_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.202',
	'username': 'Qwest',
	'password': 'ilfnb980'
}

# open a file called iosv_l2_cisco_design

with open('iosv_l2_cisco_design') as f:
	lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
        print ("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print (output)