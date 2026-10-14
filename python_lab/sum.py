ls=[]
n=int(input("enter the limit"))
for i in range(n):
    a=int(input("enter number to enter"))
    ls.append(a)
sum=0
for i in ls:
    sum=sum+i
print(sum)
