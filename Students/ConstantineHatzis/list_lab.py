#!/usr/bin/env python

from __future__ import print_function

fruit = [u"Apples", u"Pears", u"Oranges", u"Peaches"]  # Create inital list of fruit
print(fruit)


def ask_new_fruit():
    """ Return the name of a new fruit submitted by the user """
    new_fruit = raw_input(u"Name another fruit to add to the list: ")
    new_fruit = new_fruit.decode("utf-8")
    new_fruit = new_fruit.title()  # Force title case
    return new_fruit

new_fruit = ask_new_fruit()  # Prompt user for new fruit
fruit.append(new_fruit)  # Append new fruit to fruit list
print(fruit)


def choose_fruit():
    """ Return the number corresponding the fruit in the list the user has chosen on a 1-is-first basis """
    fruit_number = raw_input(u"Which fruit do you like best? (1 - {}) ".format(len(fruit)))
    fruit_number = fruit_number.decode("utf-8")
    fruit_number = fruit_number.title()  # Force title case

    if fruit_number == u"Quit":
        # Let the user exit the prompt
        quit()
    elif fruit_number.isnumeric():
        # Check if the user input is a number and convert it to an int
        fruit_number = int(fruit_number)
        if 1 <= fruit_number <= len(fruit):
            # Check if the user input is in the range of the fruit list
            fruit_number = fruit_number
        else:
            # Prompt for user input if the previous input was out of range
            print(u"You chose a number that is out of the range of the list. Please try again.")
            fruit_number = choose_fruit()
    else:
        # Prompt user for input if the previous input was not a number.
        print(u"That is not a number. Please try again.")
        fruit_number = choose_fruit()
    return fruit_number

fruit_number = choose_fruit()  # Prompt user for fruit selection
print(u"Fruit # {} is {}".format(fruit_number, fruit[fruit_number-1]))

fruit = [u"Pineapple"] + fruit  # Add a new fruit to the front of the list
print(fruit)

fruit.insert(0, u"Plum")  # Add a new fruit to the front of the list
print(fruit)

p_fruit = []  # Initialize list of fruit starting with P
for x in fruit:
    # Create list of fruit starting with P or p (not case-sensitive)
    if x[0] == u"p" or x[0] == u"P":
        p_fruit.append(x)
print(p_fruit)

# Begin second section of List Lab

print(fruit)
fruit2 = fruit[:]
fruit2.remove(fruit2[-1])
print(fruit2)

fruit2 = fruit2 * 2
print(fruit2)


def ask_bad_fruit():
    """ Return the name of a fruit that the user doesn't like and exists in the fruit list """
    bad_fruit = raw_input(u"What fruit do you hate?")
    bad_fruit = bad_fruit.decode("utf-8")
    bad_fruit = bad_fruit.title()  # Force title case

    if bad_fruit == u"Quit":
        # Let the user exit the prompt
        quit()
    elif fruit2.count(bad_fruit) == 0:
        # Check if the user input is in the list of fruit
        print(u"That fruit is not in the list. Please try again")
        bad_fruit = ask_bad_fruit()
    else:
        bad_fruit = bad_fruit
    return bad_fruit

bad_fruit = ask_bad_fruit()

for x in range(fruit2.count(bad_fruit)):
    fruit2.remove(bad_fruit)
print(fruit2)
