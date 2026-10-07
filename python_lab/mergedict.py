mydict1={}
print("enter elements of 1st dict")
while True:
    key=input("enter a key (q to quit)")
    if key=='q':
        break
    value=int(input("enter a value"))
    mydict1[key]=value
print("enter elements of 2nd dict")
mydict2={}
while True:
    key=input("enter a key(q to quit)")
    if key =='q':
        break
    value=int(input("enter avalue"))
    mydict2[key]=value
print(mydict1|mydict2)
