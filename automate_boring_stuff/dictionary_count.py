#!/usr/bin/env python
import pprint #pretty print module
message = 'You shall not pass!'
count = {}

for c in message.upper():
	count.setdefault(c,0)
	count[c] = count[c] + 1

pprint.pprint(count)
