num=int(input("enter a number"))
orignal_num=num
sum=0
while num>0:
    digit=num%10 
    sum +=digit
    num//=10
print(sum)


