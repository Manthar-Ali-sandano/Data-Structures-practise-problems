# def num(n):
#     if n>10:
#         return
#     print(n)
#     num(n+1)
# n=int(input("enter number"))
# num(n)

def name(n):
    if n>10 or n<0:
        return
    
    print("manthar")
    name(n-1)
name(5)
