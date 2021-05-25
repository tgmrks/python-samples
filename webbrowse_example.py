#!/usr/bin/env python
import webbrowser, sys, pyperclip, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

#logging.debug('args: %s' % sys.argv[1])
#logging.debug('args len: %s' % len(sys.argv))
#logging.debug('clipboard %s' % pyperclip.paste())

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

