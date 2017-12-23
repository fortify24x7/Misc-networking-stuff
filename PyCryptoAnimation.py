import time, sys, random, string
print "\n"*2
word = """

 `   `  `    `   `  \ /  `    `   `
 -#o##-## #  ` `   - + - `  ``     `
#o()()#   `_____ `  / \ `  `    `         
|()o#`    |  |  |___ ___ ___`_ _`   `
# #   | ` |     | .'| . | . | | | `
 ##  -+-  |__|__|__,|  _|  _|_  |   `
# ` ` | `     `  `  |_|`|_| |___| `
`_____ `  `_`_ ` _ ` `    ` ` `     #
|  |  |___| |_|_| |___`_ _`___  `  ##
|     | . | | | . | .'| | |_ -|  # ##|
|__|__|___|_|_|___|__,|_  |___|  #o()o#
    `   ```  |  `  `  |___|  `# ##()()
 `    `   ~ -*- ~  ` `      ## # =##o
  `  `    `  | `   `   ` `   `   `   `"""
word_dict = {}
rate = 10
for _ in word:
	word_dict.update({_:0})
while 0 in word_dict.values():
	if random.choice(range(rate)) == 0:
		while True:
			p = random.choice(word_dict.keys())
			if word_dict[p] < 1:
				word_dict[p] = 1
				break
	out = ""
	for _ in word:
		if word_dict[_] == 0:
			out += random.choice(string.printable[:94])
		else:
			out += _
	sys.stdout.write("\r  "+out)
	time.sleep(0.08)
