"""
Using comprehension in dict/set lab

dict and set comprehension

A variation of the dict/set lab done earlier. comprehension will be
used this time to make things easier.
"""

# part 1
food_prefs = {
    "name": u"Cris",
    u"city": u"Seattle",
    u"cake": u"lemon",
    u"fruit": u"pomegranate",
    u"salad": u"chop",
    u"pasta": u"lasagna"
    }

b = food_prefs

print u"{name} is from {city}, and he likes {cake} cake,
{fruit} fruit, {salad} salad, and {pasta} pasta}"

# part 2
numb = range(16)
hexa = [hex(x) for x in numb]

hexa_dict = dict(zip(numb, hexa))
print hexa_dict

# part 3
hexa_dict = {x: hex(x) for x in range(16)}
print hexa_dict

# part 4
new_dict = {}
for key,   bam in b.items():
    new_dict[key] = bam.count(u'a')

print new_dict

# part 5
s2 = set()
s3 = set()
s4 = set()

for x in range(21):
    if x % 2 == 0:
        s2.add(x)
    if x % 3 == 0:
        s3.add(x)
    if x % 4 == 0:
        s4.add(x)

print s2
print s3
print s4
