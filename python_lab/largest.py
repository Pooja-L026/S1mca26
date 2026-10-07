n1=int(input("enter the no:"))
n2=int(input("enter  2nd no:"))
n3=int(input("enter 3rd no: "))
if n1>n2 and n1>n3:
    print(n1, "is larger")
elif n2>n1 and n2>n3:
    print(n2, "is larger")
else:
    print(n3 ,"is larger")
