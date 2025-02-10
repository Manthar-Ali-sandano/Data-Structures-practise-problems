def is_palindrome(s):
    s=s.upper()
    reversed_s=""
    for char in s:
        reversed_s = char + reversed_s
    for i in range (len(s)):
        if s[i] != reversed_s[i]:
            return False
        return True
    
    
    
input_str=input("enter a string")  
if is_palindrome(input_str):
    print(input_str, "is a palindrome" )
else:
    print(input_str,"is not palindrome")
# num=(input("enter number"))
# reversed_num=num[::-1]
# if num==reversed_num:
#     print(num,"is palindrome")
# else:
#     print(num,"is not palindrome")