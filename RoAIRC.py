import sys, time, threading, RoA, string, random, socket
from random import randint
from binascii import hexlify
import DH

Ro = RoA.RoA(False)
port = 50000
key = "savsecro"*4
user = "[%s] " %raw_input("Username: ")

try:
	socket.setdefaulttimeout(2)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("8.8.8.8", 53))
	ip = sock.getsockname()[0]
	sock.close()
except Exception as e:
	ip = "127.0.0.1"
socket.setdefaulttimeout(1000)

def header(b="",c=""):
	head = ip,b,c
	return str(head) + "\x0f"

def encrypt(msg,key):
	roa_out = Ro.encrypt(msg,key)
	return str(roa_out)
	
def decrypt(roa_in):
	try:
		roa_in = eval(roa_in)
		decrypted = Ro.decrypt(roa_in[0],roa_in[1],roa_in[2])
		return decrypted
	except Exception as e:
		pass

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def encryption_handler(packet,key):
	return packet.replace(key,"!!!key!!!")

def daemon_hound():
	while 1:
		data = s.recv(5000)
		if eval(data.split("\x0f")[0])[1] == "direct" and eval(data.split("\x0f")[0])[0] == ip:
			try:
				DH.hellman_client(eval(data.split("\x0f")[0])[2])
				v = "h_"+eval(data.split("\x0f")[0])[0].replace(".","")
				time.sleep(1)
				exec "globals()['%s'] = DH.%s" % (v,v)
				while 1:
					globals()[v] = int(globals()[v])*32+6**2
					if len(str(globals()[v])) >= 32:
						break
				globals()[v] = str(globals()[v])[:32]
				msg = raw_input("[%s] => " %eval(data.split("\x0f")[0])[0])
				pack = encrypt(user+msg,globals()[v])
				pack = encryption_handler(pack,globals()[v])
				s.sendto(header(eval(data.split("\x0f")[0])[0],"dm")+pack,("255.255.255.255", port))
			except:
				pass
			globals()["stop"] = True
		
		elif eval(data.split("\x0f")[0])[2] == "dm" and eval(data.split("\x0f")[0])[0] == ip:
			print
			print decrypt(data.replace("!!!key!!!",globals()[v]).split("\x0f")[1])
		
		else:
			data = data.split("\x0f")
			if eval(data[0])[0] == ip:
				print
				print decrypt(data[1])

daemon = threading.Thread(target=daemon_hound)
daemon.daemon = True
daemon.start()
print "[DAEMON] SNIFFING"
time.sleep(0.5)
DH.hellman()
time.sleep(0.5)
stop = False

while 1:
	try:
		msg = raw_input("\n=> ")
	except:
		break
	data = header() + encrypt(user+msg,key)
	d_host = raw_input("HOST => ")
	direct = header("direct",d_host)
	if len(d_host) > 7:
		data = direct
	if len(msg) > 0:
		s.sendto(data, ("255.255.255.255", port))
	if len(d_host) > 7:
		while not stop:
			time.sleep(0.5)
	time.sleep(1)
	stop = False
