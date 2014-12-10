'''
list lab
part 1
'''
list_ = ["Apples", "Pears", "Oranges", "Peaches"]

print list_

add = raw_input(u"add fruit ")

list_.append(add)

print list_

pick = int(raw_input(u"give a number for that spot's fruit "))

# print u"%i is in spot %s "%list[pick - 1], pick
print u"{} is in spot {}".format(list_[pick - 1], pick)

print list_

list_.insert(0, "Durian")

print list

print "fruits that start with P"
for fruit in list_:
    if fruit[0] == "P":
        print fruit

# part 2
list_.remove("Durian")

print list_

vaporize = raw_input("Which fruit do you want to remove? ")

list_.remove(vaporize)

print list_

# part 3
list_[:]

for fruit in list_[:]:
    like = raw_input(u"Do you like %s? " % fruit)
    if like == "no":
        list_.remove(fruit)
    elif like == "yes":
        pass
    else:
        print "only yes or no"
print list_

list4 = []
for fruit in list_:
    list4.append(fruit[::-1])

print list4
