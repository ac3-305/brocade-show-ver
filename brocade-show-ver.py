
#Brocade show ver command:

import paramiko    #import modules
import time
import random
import sys
import getpass

ip_address = raw_input("Enter Brocade IP Address:\n")     #username input
username = raw_input("Enter username:\n")
password = getpass.getpass("Enter Password:\n")



a = ip_address.split('.')

if len(a) == 4 and int(a[0]) == 192 and int(a[1]) == 168 and int(a[2]) <= 2 and int(a[3]) <= 200:    # if your switches are on a particular IP range and subnet
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)
        remote_connection = ssh_client.invoke_shell()
        time.sleep(1)
        remote_connection.send("enable\n")
        remote_connection.send(username+"\n")
        remote_connection.send(password+"\n")
        #ssh_client.connect(username,password)
        remote_connection.send("terminal length 0\n")
        remote_connection.send("show ver\n")
        time.sleep(1)
        output = remote_connection.recv(65535)
        print output                                                                         # output confirmation
        ssh_client.close





else:
        print "\This IP is not configured for SSH connections. Please retry\n"

~                                                                                                                   
