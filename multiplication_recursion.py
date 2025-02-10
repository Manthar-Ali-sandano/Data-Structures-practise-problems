def multiplication(n):
    if n<=0:
        return 1
    m= n*multiplication(n-1)
    return m
n=int(input("enter a number"))
print("multiplication is ",multiplication(n))
