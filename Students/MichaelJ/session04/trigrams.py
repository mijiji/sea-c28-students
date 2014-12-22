"""
A method to creating new word combinations.

Trigram

Will use 3 adjacent words, the first 2 words will be a key and
the 3rd word will be the possible outcome. Thus its purpose is to create
pseudo books.
"""


from nltk.util import ngrams
text = "One night--it was on the twentieth of March, 1888"
n = 3
trigrams = ngrams(text.split(), n)
for i in trigrams:
    print i
