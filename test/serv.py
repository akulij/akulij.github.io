#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
sock = socket.socket()
sock.bind(('', 9090))
while True:
 sock.listen(1)
 conn, addr = sock.accept()
 print 'connected:', addr
 data = conn.recv(1024)
 conn.send(data.upper())

conn.close()
