#!/usr/binenv python
import traceback
try:
	raise Exception('This is a message error.')
except:
	logFile = open('error_file.log', 'a')
	logFile.write(traceback.format_exc())
	logFile.close()
