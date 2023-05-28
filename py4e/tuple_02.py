d = {'a':10, 'b':1, 'c':20}
d.items()
sorted(d.items())
#use sorted
d = {'a':10, 'b':1, 'c':20}
t = sorted(d.items())
t

for k,v in sorted(d.items()):
    print(k,v)

#sort by values instead of key
a = {'a':10, 'b':1, 'c':20}
tmp = list()
for k, v in a.items() :
    tmp.append( (v,k) )
print (tmp)
#reverse=True is descending oder
tmp = sorted(tmp, reverse=True)
print(tmp) 

#Even shorter version
d = {'a':10, 'b':1, 'c':20}
print(sorted( {(v,k) for k,v in d.items() } ) )