from os import *
from sys import *
import time
import threading
import itertools
import sys
import socket
import urllib2
import requests
import console
import speech
from requests.auth import HTTPDigestAuth
print ""
print "####################################"
console.set_color(0, 255, 255)
print "__          _______                 "
print "\ \        / /  __ \ /\             "
print " \ \  /\  / /| |__) /  \   _ __ ___ "
print "  \ \/  \/ / |  ___/ /\ \ |  __/ _ \ "
print "   \  /\  /  | |  / ____ \| | | (_)| "
print "    \/  \/   |_| /_/    \_\_|  \___/ "
print ""
console.set_color()
print "####################################"
time.sleep(2)
print ""
console.set_color(0, 255, 255)
print "WPA-ro is a Python WPA/WPA2 Key Algorithm Decrypter!\n\nMade by: SavSec\nSavageOfficial Security\n"
speech.say("WPA Ro is a WPA and a WPA2 Key Algorithm de crypt er.")
speech.say("Made by, Sav Sec.")
if len(sys.argv) < 0:
	sys.argv[1] = "1"
if len(sys.argv) > 1:
	speech.say("Remember, stealing credit for this program will result in devine punishment. Your friends and family will not be save. Bank records, crim null records, location history, and password data will all be leaked from your firneds and familys accounts. Followed by bank curruption, fires, painful poop, and never getting laid for the rest of your life. You have been warned. Please enjoy the rest of our program!")
time.sleep(2)
usr = "admin"
console.set_color()
host = raw_input("Host: ")
port = input("Port: ")
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
		console.set_color(0, 255, 255)
		print "Attempts: %s"%(sent)
		print "Timeout\n"
		print "SavSec (c) 2016 WPA-ro"
		console.set_color()
		break
	else:
		sent = sent + 1
		import os
		key = os.urandom(bits).encode('hex')
		print "Key (%s Bits):\n%s\n"%(bits, key)
