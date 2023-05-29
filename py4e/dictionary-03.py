# This code is taking a line of text as input from the user, splitting it into individual words, and
# then counting the frequency of each word using a dictionary. The `counts` dictionary is initialized
# as an empty dictionary, and then a `for` loop is used to iterate through each word in the `words`
# list. For each word, the code checks if it already exists in the `counts` dictionary using the
# `get()` method. If the word is not already in the dictionary, it is added with a value of 0. Then,
# the count for that word is incremented by 1. Finally, the code prints out the resulting dictionary
# with the word counts.
# Counting pattern
counts = dict()
line = input ('Enter a line of text:')
words = line.split()

print('Words:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

# The code is demonstrating how to use definite loops with dictionaries in Python. It first creates a
# dictionary called `counts` with some key-value pairs, and then uses a `for` loop to iterate through
# the keys in the dictionary and print out each key-value pair. It then demonstrates how to retrieve
# information from a dictionary using methods like `keys()`, `values()`, and `items()`.
# Definite loops and dictionaries
counts = {'happy ': 100, 'Lucky' : 200, 'Cute' : 10}
for key in counts:
    print (key, counts[key])

# Retrieving list of keys and values
# This code is demonstrating how to retrieve information from a dictionary in Python.
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

# Two iteration variables
# This code is iterating through the items in the dictionary `jjj` and printing out each key-value
# pair. The `for` loop uses two iteration variables `aaa` and `bbb` to represent the key and value of
# each item in the dictionary. The `print` statement then prints out the key and value for each item
# in the dictionary.
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)