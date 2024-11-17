n=int(input("enter num"))
n1=int(input("enter num"))
for i in range(1,min(a, b) + 1):
    if n%i==0 and n1%i==0:
        print("GCD = ",i)
    else:
        print("GCD = ",1)