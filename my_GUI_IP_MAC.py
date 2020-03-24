# how to find ip address and mac address


import tkinter as tk
from tkinter.messagebox import showinfo
import socket
from getmac import getmac

win = tk.Tk()
win.config(bg="#F1C40F")
win.title("Dale is a bad ass Programmer")

# find IP Address
def ip():
	hostname = socket.gethostname()
	ip_add = socket.gethostbyname(hostname)
	showinfo("IP Address",f"IP Address : {ip_add}")

# find MAC address
def mac():
	mac_add = getmac.get_mac_address()
	showinfo("MAC Address",f"MAC Address : {mac_add}")

# create buttons

ip_button = tk.Button(win,text="Show IP Address",bg="#000000",fg="#F1C40F",
					font=("times new roman",16,"bold"),command=ip)

ip_button.pack()

mac_button = tk.Button(win,text="Show MAC Address",bg="#000000",fg="#F1C40F",
	font=("times new roman",16,"bold"),command=mac)

mac_button.pack()

win.mainloop()

