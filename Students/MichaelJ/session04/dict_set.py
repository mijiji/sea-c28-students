"""
Creates a dictionary set.

Dict/Set Lab

This program creates a dictionary containing, "name", "city", "cake".
You will be able to add and delete entries.
"""

# part 1
db = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"}

print db

del db["cake"]

print db

db["fruit"] = "Mango"

print db

print db.keys()

print db.values()

print "cake" in db

print "Mango" in db.values()

# part 2 dict, 0-16, hexadecimal
numb = range(16)

hexa = []

for inte in numb:
    hexa.append(hex(inte))

hexa_db = dict(zip(numb, hexa))

print hexa_db

# part 3, number of A
a_db = {}

for key, val in db.items():
    a_db[key] = val.count('a')

for key, val in db.items():
    db[key] = val.count('a')

print db

# part 4 s2, s3, s4
s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print s2
print s3
print s4

# subset
print s3.issubset(s2)

print s4.issubset(s2)

# set with python
a = set('Python')
a.add('i')
print a

b = frozenset('marathon')

print "union of a and b: ", a.union(b)

print "intersect of a and b: ", a.intersection(b)
