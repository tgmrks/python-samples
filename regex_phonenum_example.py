#!usr/bin/env/ python3
import re
message = 'Call me at 455-555-0099 tomorrow, or at 455-555-1288'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumFound = phoneNumRegex.findall(message)
print(phoneNumFound)
