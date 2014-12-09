'''
list lab
part 1
'''
list = ["Apples", "Pears", "Oranges", " Peaches"]

print list

add = raw_input(u"add fruit ")

list.append(add)

print list

pick = int(raw_input(u"give a number for that spot's fruit "))

print u"%f is in spot %p"%(list(pick - 1, pick))

print list

list.inser("Durian", 0)

print list

print "fruits that start with P"
for fruit in list:
    if fruit[0] == "P"
        print fruit