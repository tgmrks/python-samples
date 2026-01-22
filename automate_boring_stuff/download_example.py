#!/usr/bin/env python
import requests

req = requests.get('https://automatetheboringstuff.com/files/rj.txt')
req.raise_for_status()
downloadFile = open('/home/isma/dev/python/download_file_test.txt', 'wb')

for chunck in req.iter_content(100000): # write each 100kb at a time
	downloadFile.write(chunck)

downloadFile.close()

print('Download sample: \n' + req.text[:100])
