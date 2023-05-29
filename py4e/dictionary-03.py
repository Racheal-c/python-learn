# Counting pattern
counts = dict()
line = input ('Enter a line of text:')
words = line.split()

print('Words:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

# Definite loops and dictionaries
counts = {'happy ': 100, 'Lucky' : 200, 'Cute' : 10}
for key in counts:
    print (key, counts[key])

# Retrieving list of keys and values
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

# Two iteration variables
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)