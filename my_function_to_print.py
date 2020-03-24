# use a function to print values
#
#
def print_ip(ip_addr,username,password):
    print ("My IP address is: {}" .format(ip_addr))
    print (username)
    print (password)
    print ("\n")
    return

print_ip('192.168.1.1', 'admin', 'p@ssw0rd')
print_ip('10.0.0.1', password='Cisco12345', username='dschulz')