#!/usr/bin/env python

fruit = [u'apples', u'pears', u'oranges', u'peaches']
print fruit[0]
print fruit[1]
print fruit[2]
print fruit[3]
#Instructors: can't find a better way to code this to print the list as a list of words, not u'oranges', u'apples', etc...

fruit.append(raw_input(u'Please add a fruit:     '))
print fruit[0]
print fruit[1]
print fruit[2]
print fruit[3]
print fruit[4]
