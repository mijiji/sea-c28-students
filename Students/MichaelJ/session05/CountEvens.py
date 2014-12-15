"""
Creating a script to count evens.

List Comprehensions, count evens.

An exercise on list comprehensions to count even numbers in a list.
"""


def count_evens(nums):
    """
count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
return count
    """
    sum([1 for x in nums if x % 2 == 0])

print count_evens([2, 1, 2, 3, 4])
