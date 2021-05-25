#!/usr/bin/env python3
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) # deactivate all logging from critical to lower

logging.debug('Starting the program.')

def factorial(n):
	logging.debug('Start of factorial(%s)' % (n))
	total = 1
	for i in range(1, n + 1):
		total *= i
		logging.debug('i is %s, total is %s' % (i,total))

	logging.debug('retunr value %s' % (total))
	return total

print(factorial(7))
logging.debug('End of program')
