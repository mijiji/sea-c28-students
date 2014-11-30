
# This Python file contains four functions that cause these errors when called:
# NameError, TypeError, SyntaxError, AttributeError

def GenerateNameError():
    ThisShouldCauseANameError

GenerateNameError()


def GenerateTypeError():
    a = "One"
    b = 2
    print(a + b)

GenerateTypeError()

def GenerateSyntaxError():
    This is a bad symbol = 1

GenerateSyntaxError()

#This function causes an AttributeError when it is defined, not when it is called.
def GenerateAttributeError():
    i = 4;
    j = i.length();

GenerateAttributeError()
