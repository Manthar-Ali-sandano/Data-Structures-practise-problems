def num(n):
    if n>10:
        return
    print(n)
    num(n+1)
n=int(input("enter number"))
num(n)
