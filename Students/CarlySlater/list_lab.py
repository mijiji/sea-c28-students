#!/usr/bin/env python

fruit = [u'apples', u'pears', u'oranges', u'peaches']
for i in fruit:
    print i

#ask the user for a number and display the number back to the user and the fruit corresponding to that number (ona 1-is basis)


fruit.append(raw_input(u'Please add a fruit:     '))
for i in fruit:
    print i

usernumber = input(u'choose a number from 1 to 5:     ')

print usernumber
print fruit[(usernumber-1)]

print ""
fruit = ([u'kiwi'] + fruit)
for i in fruit:
    print i
print ""
fruit.insert(0, u'pomelo')
for i in fruit:
    print i
print ""
print u'all the fruits that begin with the Letter P:    '
print ""

#display all fruits beginning with P:
for i in fruit: 
    if u'p' == i[0] : 
        print i
print ""
print ""
print ""

#PART 2 of the ASSIGNMENT:

print "Part 2"
# this is to differentiate the parts of the assignment while running it





