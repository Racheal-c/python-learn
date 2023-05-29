# use dictionary to count the number of things 
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
'csev' in ccc

# Dictionary tracebacks (Use in rator to see if the key is inthe dictionary)
ccc = dict()
'csev' in ccc

# Add new name to the diciionary
counts = dict()
names = ['cse', 'cwen', 'nams', 'cse', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
    print(counts)

# Get is a method not a function for dictionary to check the key is already in a dictionary
if name in counts:
    x = counts[name]
else:
    x = 0
# EQUIVALENT WITH THE CODE ABOVE THIS
x = counts.get(name,0)

# Simplify counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    # '00 here os the deafult value
    counts[name] = counts.get(name, 0) + 1
print(counts)