#!/usr/bin/env python
def div42by(num) :
	try :
		return 42 / num
	except ZeroDivisionError : # specific exception error
		print('Error: can\'t devide by zero')
	except : # generic exception
		print('Error: sth went wrong in the code')

print(div42by(2))
print(div42by(0))
print(div42by(10))
print(div42by('a'))
print(div42by(3))
