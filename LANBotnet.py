import socket, time, random, string, sys, argparse

import argparse, sys
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",help="Server Verbose", action="store_true")
parser.add_argument("-s", "--servers",help="Make Random Servers", type=int, default=0)
parser.add_argument("-n", "--nohelp",help="Disable Help", action="store_true")
args = parser.parse_args()

if not args.nohelp:
	parser.print_help()
	print ""

verbose = args.verbose
srvs = args.servers

servers = [
	[" End Of School Year! I Made 1000 Servers!", 420]
]

if srvs > 0:
	servers = []
	for i in range(1,srvs):
		servers.append([str(i+1) + " " + "".join(random.sample(string.ascii_letters,15)), random.choice(range(10000,31000))])

BROADCAST_IP = "255.255.255.255"
BROADCAST_PORT = 4445

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("",BROADCAST_PORT))
socket.setdefaulttimeout(1)

print "\n - Broadcasting Minecraft Servers - \n"
for i in range(len(servers)):
	sys.stdout.write("\rTotal Servers: "+str(i+1))
if verbose:
	print "\n"
	for s in servers:
		print s
else:
	for s in servers:
		sys.stdout.write("\r"+str(s))
		time.sleep(100/len(servers))
	print ""

def checksum():
	print "\n[+] Running Checksum"
	time.sleep(1)
	a = 0
	global data
	global found
	data = []
	found = []
	try:
		for server in servers:
			msg = "[MOTD]%s[/MOTD][AD]%d[/AD]" % (server[0], server[1])
			sock.sendto(msg, (BROADCAST_IP, BROADCAST_PORT))
			data.append(sock.recv(100))
			found.append(msg)
			time.sleep(0.005)
		for c in found:
			if c in data:
				a = a + 1
				sys.stdout.write("\r[+] Confirmed %s of %s Servers" %(a+1,len(servers)+1))
				time.sleep(0.005)
	except:
		pass
	sys.stdout.write("\r[+] Confirmed %s of %s Servers\n" %(a+2,len(servers)+1))
	if a == 0:
		print "[-] Exiting - No Connection"
		sock.close()
		sys.exit()
	elif verbose:
		print " - Missing Servers - "
		for f in data:
			if f not in found:
				print f[0]
			else:
				note = True
		if note: print "		  None"
	print "[+] Keeping Servers Up"

check = True
b = 0
while 1:
	for server in servers:
		try:
			msg = "[MOTD]%s[/MOTD][AD]%d[/AD]" % (server[0], server[1])
			sock.sendto(msg, (BROADCAST_IP, BROADCAST_PORT))
		except KeyboardInterrupt:
			print "\n[+] Stopping Servers"
			sock.close()
			sys.exit()
		except:
			b = b + 1
			sys.stdout.write("\r[-] Failed %s Time(s)" %(b))
			pass
		if check:
			checksum()
		check = False
	time.sleep(1.5)
