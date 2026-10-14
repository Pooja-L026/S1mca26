n=int(input("ENTER NO OF N TERMS:"))
if n<=0:
    print("not defined")
else:
   first=0
   second=1
   print("FIBONACCI SERIES: ")
   for i in range(2,n):
        fib=first+second
        first=second
        second=fib
        if fib>n:
            break
        if i==n-1:
            print(fib,end=" ")
        else:
            print(fib,end=",")
            
    
    
    

    
