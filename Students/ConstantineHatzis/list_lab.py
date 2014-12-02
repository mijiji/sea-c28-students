#!/usr/bin/env python

from __future__ import print_function

fruit = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

print(fruit)

new_fruit = raw_input(u"Name another fruit to add to the list: ")

fruit.append(new_fruit.decode("utf-8"))

print(fruit)
