#!/usr/bin/env python

import socket
import subprocess
import os , sys
import shutil
import time
sock = socket.socket()
sock.bind(('', 8181))
port=1100
print os.listdir(os.getcwd())
while True:

 def clientAdd():
  client=open(clientname,'w')
  client.write(clienttext)
  client.close()
  client=open(clientname,'a')
  client.write(ipv)
  client.close()
  client=open(clientname,'a')
  client.write(ad)
  client.close()
  client=open(clientname,'a')
  client.write(str(port))
  client.close()
  client=open(clientname,'a')
  client.write(ad1)
  client.close()
  client=open(clientname,'a')
  client.write(ip)
  client.close()
  client=open(clientname,'a')
  client.write(ad2)
  client.close()
 print ' '
 sock.listen(1)
 conn, addr = sock.accept()
 print 'connected:', addr
 data = conn.recv(1024)
 #conn.send(data.upper())
 conn.send('connected')
 print data
 ip=str(addr)
 ip=ip[2:-9]
 clientname=ip+'.py'
 def clientCreate():
  a=6
 ipv="'"+ip+"'"
 clienttext='''
import socket
import os
sock = socket.socket()
sock.connect(('''
 ad=''','''
 ad1='''))
comnd=raw_input('Command: ')
if comnd=='exit':
  a=6
elif comnd=='stop':
  sock.send(comnd)
  sock.close()
else:
  sock.send(comnd)
  data = sock.recv(1024)#continue this
  print data
  os.system('python '''
 ad2=".py')"
 clientAdd()
 if not os.path.isfile(clientname):
  print 'NEW user'
  print ' '
  clientCreate()
 else: 
  print 'this user is was'
  print ' '
conn.close()

