"""
Creates a dictionary set.

Dict/Set Lab

This program creates a dictionary containing, "name", "city", "cake".
You will be able to add and delete entries.
"""


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

