#!/usr/bin/env python
import re
mypws = 'pw base patterns: base1: tgmrks base2: stgadmin'
print('original text:\n' + mypws)
pwre = re.compile(r'base\d:\s(\w)\w+') 
print('regex result:')
print(pwre.findall(mypws))
print('modified text:')
print(pwre.sub(r'base: \1*****',mypws))
