#!/usr/bin/python

import sys
import socket
import argparse

parser = argparse.ArgumentParser(description ='Send HTTP methods to a URL')
parser.add_argument('host')
parser.add_argument('method')
parser.add_argument('URI', nargs='?', default='/')
parser.add_argument('port', type=int, nargs='?', default=80)
args = parser.parse_args()

messages={'get': "GET ", 'options': "OPTIONS ", 'head': "HEAD ", 'trace': "TRACE ", 'put': "PUT ", 'connect': "CONNECT "}

try:
	args.method in messages
except:
	print 'Invalid method. Methods are: get, options, head, trace, put, connect'
	sys.exit()
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print 'Socket creation failed'
	sys.exit()
try:
	ip = socket.gethostbyname(args.host)
except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

s.connect((ip, args.port))
endmsg = args.URI+" HTTP/1.1\r\nHOST: "+args.host+ "\r\n\r\n"
message = messages[args.method] + endmsg

try: 
	s.sendall(message)
except socket.error:
	print 'Send Failed'
	sys.exit()

reply = s.recv(4096)
print reply

s.close()

