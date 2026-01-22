#!/usr/bin/env python

# range(start, end, step) 

print('counting up to 5')
for i in range(5) :
    print('hello ' + str(i))

print('counting up to 10 w/ 2 steps')
for i in range(0,10,2) :
    print('hello ' + str(i))

print('counting down from 12 t0 0 w/ 3 steps')
for i in range(12,0,-3) :
    print('hello ' + str(i))

print('sum up range of even number from 0 to 100')
spam = list(range(0, 100, 2))
sum = 0
for i in range(len(spam)):
	sum = sum + spam[i]

print('Total sum: ' + str(sum))
