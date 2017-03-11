#operation to create csv list from text list

name = "OSTPmove161207.txt"

handle = open(name, 'r')
#cfile = []
stringOut = ""
#lineCount = 0



for line in handle:
	if line.startswith(""):
		stringOut = stringOut+ ", " +line.strip()
	else:
		continue

#print cfile
print stringOut
