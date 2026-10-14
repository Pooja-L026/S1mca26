result=[]

start=int(input("enter 4 digit no:"))
end=int(input("enter last 4 digit:  "))

if start<1000 or end >9999 or start>end:
    print("Invalid")
else:
    for num in range(start,end+1):
        if num%2 == 0:
            root=int(num**0.5)
            if root*root== num:
                result.append(num)
print(result)
