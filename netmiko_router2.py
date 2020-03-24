# this script:
#      prompts the user for name and password
#      opens a file called commands_list
#      opens a file called devices_list
#      logs in to each router in the list
#      (this script adds exception handling !!)
#      does a show ip interface brief
#      executes the commands from the file
#      one line at a time 
#
from getpass import getpass
import sys
from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
#from paramiko.ssh_exception import SSHExcecption
from netmiko.ssh_exception import AuthenticationException


# with open('commands_file.txt') as f:
#	commands_list = f.read().splitlines()
with open("commands_file.txt") as f:
    commands_list = f.readlines()

with open('devices_file.txt') as f:
	devices_list = f.read().splitlines()	

for devices in devices_list:
	print ("Connecting to device " + devices)
	ip_address_of_device = devices
	ios_device = {
	    'device_type': 'cisco_ios',
	    'ip': ip_address_of_device,
	    'username': 'Qwest',
	    'password': getpass()
    }

try:
    net_connect = Netmiko(**ios_device)
except (AuthenticationException):
    print ("Authentication failure: " + ip_address_of_device)
except (NetMikoTimeoutException):
    print ("Timeout to device: " + ip_address_of_device)
except (EOFError):
    print ("End of file while attempting " + ip_address_of_device)
except (SSHExcecption):
    print ("SSH Issue. Are you sure SSH i" + ip_address_of_device)
except Exception as unknown_error:
    print ("Some other error: " + unknown_error)

output = net_connect.send_command(commands_list)
print (output)

#for n in range (2,21):
#    print ("Creating VLAN " + str(n))
#    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
#    output = net_connect.send_config_set(config_commands)
#    print (output)
