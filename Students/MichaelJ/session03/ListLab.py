'''
list lab
part 1
'''
list = ["Apples", "Pears", "Oranges", "Peaches"]

print list

add = raw_input(u"add fruit ")

list.append(add)

print list

pick = int(raw_input(u"give a number for that spot's fruit "))

# print u"%i is in spot %s "%list[pick - 1], pick
print u"{} is in spot {}".format(list[pick - 1], pick)

print list

list.insert(0, "Durian")

print list

print "fruits that start with P"
for fruit in list:
    if fruit[0] == "P":
        print fruit

# part 2
list2 = list[:]
list2.remove("Durian")

print list2

vaporize = raw_input("Which fruit do you want to remove? ")

list2.remove(vaporize)

print list2

# part 3
list3 = list[:]

for fruit in list3:
    like = raw_input(u"Do you like %s? " % fruit)
    if like == "no":
        while fruit in list3:
            list3.remove(fruit)
    elif like == "yes":
        pass
    else:
        print "only yes or no"
print list3

list4 = []
for fruit in list:
    list4.append(fruit[::-1])

print list4
