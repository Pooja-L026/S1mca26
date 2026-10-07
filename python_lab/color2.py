n1=int(input("enter the no of colors in first list"))
ls1=[]
for i in range (n1):
            a=input("enter name of color:")
            ls1.append(a)
n2=int(input("enter the no of colorsin second list"))
ls2=[]
for i in range (n2):
             b=input("enter color:")
             ls2.append(b)
print("Colors in s1 not in s2",set(ls1)-set(ls2))
