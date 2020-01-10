#Compare line by line code
#Developer :Dushmanta

from pathlib import Path


# Open file for reading in text mode (default mode)
f1 = open('/file1.txt','r')
f2 = open('/file2.txt','r')


# Read the first line from the files
old_lines = f1.readline()
new_lines = f2.readline()

old_lines_set = set(old_lines)
new_lines_set = set(new_lines)

old_added = old_lines_set - new_lines_set
old_removed = new_lines_set - old_lines_set

for line in old_lines:
	if line in old_added:
		print ('-', line.strip())
	elif line in old_removed:
		print ('+', line.strip())

for line in new_lines:
	if line in old_added:
		print ('-', line.strip())
	elif line in old_removed:
		print ('+', line.strip())


