import operator
mydict={}
while True:
    key=input("enter a key(q to quit)")
    if key=='q':
      break
    value=int(input("enter a value"))
    mydict[key]=value
print('Original dictionary: ',mydict)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1)))
print('Ascending order : ',sd)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=True))
print('Descending order: ',sd)
