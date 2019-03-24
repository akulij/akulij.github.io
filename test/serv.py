#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
sock = socket.socket()
sock.bind(('', 9090))
while True:
 sock.listen(1)
 conn, addr = sock.accept()
 print 'connected:', addr
 data = conn.recv(10240)
 #conn.send(data.upper())
 conn.send('''HTTP/1.1 400 Bad Request
 Server: nginx/1.10.3 (Ubuntu)
 Date: Wed, 13 Mar 2019 10:57:38 GMT
 Content-Type: text/html
 Content-Length: 182
 Connection: close
 
 <html>
 <head><title>400 Bad Request</title></head>
 <body bgcolor="white">
 <center><h1>400 Bad Request</h1></center>
 <hr><center>nginx/1.10.3 (Ubuntu)</center>
 </body>
 </html>
 ''')
 print data
conn.close()
