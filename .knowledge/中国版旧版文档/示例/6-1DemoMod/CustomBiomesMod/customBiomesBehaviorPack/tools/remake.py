import sys
dim = sys.argv[1]

import os
import shutil
shutil.copytree("template", dim)

dirpath, dirnames, filenames = os.walk(dim).next()
for fname in filenames:
	fullPath = os.path.join(dirpath, fname)
	
	with open(fullPath, 'r') as f:
		fstr = f.read()
	fstr = fstr.replace('dm3', dim)
	with open(fullPath, 'w') as f:
		f.write(fstr)
	
	os.rename(fullPath, os.path.join(dirpath, dim + fname[3:]))
