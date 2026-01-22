#!/usr/bin/env python
import os

for folderName, subFolders, fileNames in os.walk('/home/isma/dev/'):
	print('Folder: ' + str(folderName))
	print('Sub Folders: ' + str(subFolders))
	print('files: ' + str(fileNames))
	print()
	for file in fileNames:
		if(file.endswith('.py')):
		 	print('you have some Python code here :)')
