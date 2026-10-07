c=int(input("enter limit"))
li=[]
for i in range(c):
    a=int(input("Enter elemnts"))
    li.append(a)
for i in li:
    if(i%2==0):
        li.remove(i)
print(li)
