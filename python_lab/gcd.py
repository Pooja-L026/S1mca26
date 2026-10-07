def findgcd(a,b):
    while b:
        a,b=b,a%b
    return a
n1=int(input("enter first no: "))
n2=int(input("enter sec no: "))
gcd=findgcd(n1,n2)
print(f"The GCD of {n1}and {n2} is {gcd}")
