#!/usr/bin/python

import sys
import socket



port = 80

if len(sys.argv) < 3:
	sys.exit('Usage: python bannerman.py [host] [method] (optional)[uri]\r\nAllowed methods: get, options, put, trace, head, connect')
elif len(sys.argv) == 3:
	host = sys.argv[1]
	URI = '/'
elif len(sys.argv) == 4:
	host = sys.argv[1]
	URI = sys.argv[3]
else:
	sys.exit('Too many arguements. Usage: python bannerman.py [host]')

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print 'Socket creation failed'
	sys.exit()
try:
	ip = socket.gethostbyname(host)
except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

s.connect((ip, port))
endmsg = URI+" HTTP/1.1\r\nHOST: "+host+ "\r\n\r\n"
messages = {'get': "GET ", 'options': "OPTIONS ", 'head': "HEAD ", 'trace': "TRACE ", 'put': "PUT ", 'connect': "CONNECT "}
message = messages[sys.argv[2]] + endmsg


try: 
	s.sendall(message)
except socket.error:
	print 'Send Failed'
	sys.exit()

reply = s.recv(4096)

print reply
s.close()
