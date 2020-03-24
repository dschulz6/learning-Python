#!/Python37-32
"""

open a text file called requirements.txt
format and display text to screen

"""
with open("requirements.txt") as f:
	output = f.readlines()
print()
#print (output)
#
a = output[0]
b = output[1]
c = output[2]
d = output[3]
e = output[4]
f = output[5]
g = output[6]
h = output[7]
#
print ("-" * 20)
print (a,b,c,d,e,f,g,h)
print ()


