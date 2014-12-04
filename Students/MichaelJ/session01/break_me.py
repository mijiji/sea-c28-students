sqrt(9)
# NameError: name 'sqrt' is not defined

a + b = 4
# SyntaxError: can't assign to operator

len(4, 2, 5)
'''
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    len(4,2,5)
TypeError: len() takes exactly one argument (3 given)
'''

dog = 8
dog.upper()
'''
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dog.upper()
AttributeError: 'int' object has no attribute 'upper'
'''