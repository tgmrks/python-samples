#!/usr/bin/env python
def spam() :
	global bacon
	bacon = 23
	print('bacon from global: ' + str(bacon))
	eggs = 99
	print('eggs from local: ' + str(eggs)) # eggs here is the local assigned above

eggs = 42
bacon = 0
spam()
print('this is eggs in global: ' + str(eggs)) # will print the global
print('this bacon in global:  ' + str(bacon)) # bacon was changed in bc of the global statem. 

