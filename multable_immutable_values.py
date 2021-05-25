#!/usr/bin/env python
def eggs(someEggs) :
	someEggs.append('spam')

spam = ['bacon','sausage','egg']
print(spam)
eggs(spam)
print(spam)

# even though 'someEggs' is destroyed after the function ends for not being a global variable
# it's only receiving the reference to the list 'spam', not the actual value.
# what was append in to the memory, which will reflect to the same result 'spam' is referring
# 'spam' and 'someEggs' are mutable, their value is stored in memory
# a string for instance is immutable, its value must be reassigned in place
