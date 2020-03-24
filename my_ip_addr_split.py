ip_addr = "192.168.1.200"
#
x = ip_addr.split(".")
a = x[0]
b = x[1]
c = x[2]
d = x[3]
#
#
print (ip_addr)
print()
# print 80 hyphens
print ("-" * 80)
print (a)
print (b)
print (c)
print (d)
print ("-" * 80)
# print each octet in columns 20 char wide
print ("{:20}{:20}{:20}{:20}".format(x[0], x[1], x[2], x[3]))
print()
