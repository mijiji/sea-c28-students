#!/usr/bin/env python

fruit = [u'apples', u'pears', u'oranges', u'peaches']
for i in fruit:
    print i


#Instructors: can't find a better way to code this to print the list as a list of words, not u'oranges', u'apples', etc...

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


