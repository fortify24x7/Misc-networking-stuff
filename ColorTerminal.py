# Version 9.0.1 Omega
# Made for Pythonista 3
# By: SavSec
# - I Don't Give A Fuck License -
# AutoStablize v2: PotatoGod
# AutoStablize Debugging: SavSec

import clipboard, random, sys, os, time, console

rainbowfade = ["#ff0000","#ff4909","#ff7100","#ffac00","#eeff00","#b1ff00",'#27ff00','#09ff00','#00ff21','#00ff9b','#00ffd8','#00deff','#009bff','#0059ff','#0016ff','#5700ff','#b100ff','#f400ff','#ff00c8','#ff0085','#ff0043']
bloodfade = ["#cc0000","#bb0000","#aa0000","#990000","#880000","#770000","#880000","#990000","#aa0000","#bb0000"]
bluefade = ["#0000cc","#0000bb","#0000aa","#000099","#000088","#000077","#000088","#000099","#0000aa","#0000bb"]
rainbow = ["#ff0000","#ff8500","#f2ff00","#00ff00","#00ffff","#0000ff","#ff00ff"]

def bloodforum():
	# BloodForum is used on Hacker's Forum Page To Make Blood Text
	try:
		colors = ["#e00000","#c70000","#af0000","#a10000","#8e0000","#7d0000","#a00000","#ad0000","#ca0000","#e00000"]
		new = ""
		s = 0
		a = 0
		n = 2
		while 1:
			msg = unicode(raw_input("Message: "))
			if msg == "!quit":
				break
			msg = [msg[i:i+n] for i in range(0, len(msg), n)]
			for _ in msg:
				if s == 10:
					s = a
					a = 1
					if a == 10:
						a = 0
				if _ == " ":
					new = new + _
					s = s - 1
				else:
					new = new + "[color=" + colors[s] + "]" + _ + "[/color]"
				s = s + 1
			clipboard.set(new)
			new = ""
	except:
		pass

def updown():
	# UpDown Makes Your Text Go Up And Down
	colors = ["#sup","#/sup","#sub","#/sub"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = unicode(raw_input("Message: "))
			if msg == "!quit":
				break
			if len(msg) >= 100:
				msgb = msg[100:]
				msg = msg[:100]
			msg = msg.split(" ")
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == " ":
					new = new + " "
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + _ + " "
				s = s + 1
			clipboard.set("[c][b][efffff]" + new + msgb)
			new = ""
			msgb = ""
	except:
		pass

def captcha():
	# Makes text almost impossible to read
	colors = ["#i","#/i","#i","#/i"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = unicode(raw_input("Message: ").replace("a","4").replace("e","3").replace("t","7").replace("i","1").replace("o","0").replace("B","8").replace("s","5"))
			if msg == "!quit":
				break
			if len(msg) >= 100:
				msgb = msg[100:]
				msg = msg[:100]
			msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == " ":
					new = new + " "
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + _
				s = s + 1
			clipboard.set("[c][b][efffff]" + new + msgb)
			new = ""
			msgb = ""
	except:
		pass

def italics():
	# italics or not italics, which one?
	colors = ["#i","#/i","#i","#/i"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = unicode(raw_input("Message: "))
			if msg == "!quit":
				break
			if len(msg) >= 100:
				msgb = msg[100:]
				msg = msg[:100]
			msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == " ":
					new = new + " "
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + _
				s = s + 1
			clipboard.set("[c][b][efffff]" + new + msgb)
			new = ""
			msgb = ""
	except:
		pass

def liner():
	# so many lines!
	colors = ["#u","#/u","#u","#/u"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = unicode(raw_input("Message: "))
			if msg == "!quit":
				break
			if len(msg) >= 100:
				msgb = msg[100:]
				msg = msg[:100]
			msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == " ":
					new = new + " "
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + _
				s = s + 1
			clipboard.set("[c][b][efffff]" + new + msgb)
			new = ""
			msgb = ""
	except:
		pass

def undercolor():
	# Undercolor Provides a Under Beam of Colour
	colors = ["#ff0000"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = unicode(raw_input("Message: "))
			if msg == "!quit":
				break
			if len(msg) <= 11:
				n = 1
			elif 11 < len(msg) <= 18:
				n = 2
			elif 18 < len(msg) <= 32:
				n = 3
			elif 32 < len(msg) <= 50:
				n = 5
			msg = [msg[i:i+n] for i in range(0, len(msg), n)]
			if len(msg) >= 25:
				msgb = msg[25:]
				msg = msg[:35]
			msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
				new = new + colors[s].replace("#","[") + "]" + u"\u0332" + "[efffff]" + _
				s = s + 1
			clipboard.set("[c][b]" + new + msgb)
			new = ""
			msgb = ""
			s = s
	except:
		pass

def l33t():
	try:
		while 1:
			clipboard.set("[c][b][00ff00]"+unicode(raw_input("Message: ").replace("a","4").replace("e","3").replace("t","7").replace("i","1").replace("o","0").replace("B","8").replace("s","5")))
	except:
		pass

def fancy(cl="ord"):
	# Font Types
	# ord - Ordered cycle through all font options
	# ran - Random choice of font options
	# rancycle - Randomly choose 1 font to cycle with
	# 1 - font 1, Candy-Cain-Like font structure
	# 2 - font 2, blue and yellow lightning-like font structure
	# 3 - font 3, black and yellow storm font structure
	# 4 - font 4, light prism font structure
	fa1 = "[c][b][efffff]-[ff0000]=[efffff]-[ff0000]=[efffff]- %s [efffff]-[ff0000]=[efffff]-[ff0000]=[efffff]-" 
	fa2 = "[c][b][0000ff]>[ffff00]> [0000ff]>[ffff00]>[efffff] %s [ffff00]<[0000ff]< [ffff00]<[0000ff]<"
	fa3 = "[c][b][ffff00]+[585858]-[484848]=[585858]-[ffff00]+[efffff] %s [ffff00]+[585858]-[484848]=[585858]-[ffff00]+"
	fa4 = "[c][b][9f9f9f]|[ffff00]: : :[9f9f9f]| [ffff00]-[efffff] %s [ffff00]- [9f9f9f]|[ffff00]: : :[9f9f9f]|"
	ord = [fa1,fa2,fa3,fa4]
	if cl == "ord":
		try:
			while 1:
				for _ in ord:
					clipboard.set(_ % unicode(raw_input("Message: ")))
		except:
			pass
	if cl == "ran":
		try:
			while 1:
				_ = random.choice(ord)
				clipboard.set(_ % unicode(raw_input("Message: ")))
		except:
			pass

def RegularMulticolor(colors):
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = unicode(raw_input("Message: "))
			if msg == "!quit":
				break
			msg = unicode(msg)
			if len(msg) >= 22:
				msgb = msg[22:]
				msg = msg[:22]
			msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == " ":
					new = new + " "
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + _
				s = s + 1
			clipboard.set("[c][b]" + new + msgb)
			new = ""
			msgb = ""
			s = 0
	except:
		pass

def AutoLength(colors):
	# RainfadeAuto Provides a Smooth Transition In Between Each Set Of Color
	# This version automatically increases the length of color as the message gets bigger
	# Auto Adjustment Code By: 
	colors = ["#ff0000","#ff4909","#ff7100","#ffac00","#eeff00","#b1ff00",'#27ff00','#09ff00','#00ff21','#00ff9b','#00ffd8','#00deff','#009bff','#0059ff','#0016ff','#5700ff','#b100ff','#f400ff','#ff00c8','#ff0085','#ff0043']
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = unicode(raw_input("Message: "))
			if msg == "!quit":
				break
			if len(msg) >= 42:
				print " - MSG too long, change it a bit (current message set to clipboard -)"
				clipboard.set(msg)
				msg = " "
			step = 0
			while 1:
				step = step + 1
				cs = step
				msg = list(msg)
				for _ in msg:
					if s >= len(colors):
						s = 0
					if _ == " " or cs < step:
						new = new + _
						s = s - 1
					else:
						new = new + colors[s].replace("#","[") + "]" + _
						cs = 0
						s = s + 1
					cs = cs + 1
				if len(new) < 210:
					break
				else:
					new = " "
			try:
				clipboard.set("[c][b]" + new)
			except:
				pass
			new = ""
			msgb = ""
			s = 0
			step = 0
			cs = 0
	except:
		pass

def colorhelp():
	print ""
	console.set_font("Arial-BoldMT",16)
	print "Commands: "
	console.set_font()
	time.sleep(0.3)
	print "Rainbow  - rainbow | r1"
	time.sleep(0.3)
	print "Rainfade - rainfade | r1"
	time.sleep(0.3)
	print "Blood    - blood | b1"
	time.sleep(0.3)
	print "BlueFade - bluefade | r1"
	time.sleep(0.3)
	print "Exit      - q | exit"
	time.sleep(0.3)
	print "Back      - cd | back"
	time.sleep(0.3)
	print "Clear     - cls | clear"
	time.sleep(0.3)
	print "\nTip: Typing \"!quit\" while using a color will return you to the command line!"

while 1:
	location = "Menu"
	act = "\n~/" + str(location) + "$: "
	console.set_color(1,1,1)
	try:
		data = raw_input(act)
	except:
		pass
	console.set_color()
	if data == "auto" or data == "a" or data == "stable":
		while 1:
			location = "AutoStablize"
			act = "\n~/" + str(location) + "$: "
			console.set_color(1,1,1)
			try:
				data = raw_input(act)
			except:
				sys.exit()
			console.set_color()
			if data == "rainbow" or data == "r1":
				RegularMulticolor(rainbow)
			if data == "rainfade" or data == "r2":
				RegularMulticolor(rainbowfade)
			if data == "blood" or data == "b1":
				RegularMulticolor(bloodfade)
			if data == "bluefade" or data == "b2":
				RegularMulticolor(bluefade)
			if data == "quit" or data == "q" or data == "exit":
				sys.exit()
			if data == "clear" or data == "cls" or data == "clr":
				console.clear()
			if data == "back" or data == "cd":
				break
			if data == "?" or data == "help":
				colorhelp()
	if data == "regular" or data == "r" or data == "reg":
		while 1:
			location = "Regular"
			act = "\n~/" + str(location) + "$: "
			console.set_color(1,1,1)
			try:
				data = raw_input(act)
			except:
				sys.exit()
			console.set_color()
			if data == "rainbow" or data == "r1":
				AutoLength(rainbow)
			if data == "rainfade" or data == "r2":
				AutoLength(rainbowfade)
			if data == "blood" or data == "b1":
				AutoLength(bloodfade)
			if data == "bluefade" or data == "b2":
				AutoLength()(bluefade)
			if data == "quit" or data == "q" or data == "exit":
				sys.exit()
			if data == "clear" or data == "cls" or data == "clr":
				console.clear()
			if data == "?" or data == "help":
				colorhelp()
			if data == "back" or data == "cd":
				break
	if data == "exit" or data == "quit" or data == "q":
		sys.exit()
	if data == "clear" or data == "cls" or data == "clr":
		console.clear()
	if data == "help" or data == "?":
		print ""
		console.set_font("Arial-BoldMT",16)
		print "Menu Commands: "
		console.set_font()
		time.sleep(0.3)
		print "Regular   - r | regular | reg"
		time.sleep(0.3)
		print "Stablized - s | auto | stable"
		time.sleep(0.3)
		print "Exit       - q : exit"
		time.sleep(0.3)
		print "Back       - cd : back"
		time.sleep(0.3)
		print "Clear      - cls : clear"
		time.sleep(0.3)
