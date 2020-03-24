# this script:
#      prompts the user for name and password
#      opens a file called commands_list
#      opens a file called devices_list
#      logs in to each router in the list
#      (this script adds exception handling !!)
#      (this version adds a check for device type router or switch
#      (and executes different commands based on device type)
#      ( this version copies the configs to a file on disk)
#      does a show ip interface brief
#      executes the commands from the file
#      one line at a time 

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHExcecption
from netmiko.ssh_exception import Authentication

# IOS version types
list_versions = ['vios_l2-ADVENTERPRISEK9-M',
                 'VIOS-ADVENTERPRISEK9-M',
                 'C1900-UNIVERSALK9-M',
                 'C3750-ADVIPSERVICESK9-M'
                 ]

#   Check software versions
    for software_ver in list_versions:
        print "Checking for " + software_ver
        output_version = net_connect.send_command('show version')
        int_version = 0 # Reset integer value
        int_version = output_version.find(software_ver)
        if int_version > 0:
            print "Software version found: " + software_ver
            break
        else:
            print "Did not find " + software_ver                  

username = input("Enter your SSH username: ")
password = getpass()

with open('commands_file_switch') as f:
	commands_list_switch = f.read().splitlines()

with open('commands_file_router') as f:
    commands_list_router = f.read().splitlines()    

with open('devices_file') as f:
	devices_list = f.read().splitlines()	

for devices in devices_list:
	print "Connecting to device" + devices
	ip_address_of_device = devices
	ios_device = {
	    'device_type': 'cisco_ios',
	    'ip': ip_address_of_device,
	    'username': username,
	    'password': password
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print 'Authentication failure: ' + ip_address_of_device
        continue
    except (NetMikoTimeoutException):
        print 'Timeout to device: ' + ip_address_of_device
        continue
    except (EOFError):
        print "End of file while attempting " + ip_address_of_device
        continue
    except (SSHExcecption):
        print 'SSH Issue. Are you sure SSH i' + ip_address_of_device
        continue
    except Exception as unknown_error:
        print 'Some other error: ' + unknown_error
        continue  

if software_ver == 'vios_l2-ADVENTERPRISEK9-M':
    print "Running " + software_ver + " commands" 
    output = net_connect.send_config_set(commands_list_switch)
elif software_ver == 'VIOS-ADVENTERPRISEK9-M':
    print "Running " + software_ver + " commands" 
    output = net_connect.send_config_set(commands_list_router)

print output        

# ------ Write out configuration information
config_filename = 'config-' + device['ipaddr']

print ("-----Writing configuration: ", config_filename
with open(config_filename, 'w') as config_out: config_out.write(config_data)

session.disconnect
    

#for n in range (2,21):
#    print ("Creating VLAN " + str(n))
#    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
#    output = net_connect.send_config_set(config_commands)
#    print (output)