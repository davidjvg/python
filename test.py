
import os
for x in os.listdir('c:/Windows/system32'):
	if x[-3:] == 'exe' or x[-3:] == 'msi' or x[-3:] == 'pl':
		print x