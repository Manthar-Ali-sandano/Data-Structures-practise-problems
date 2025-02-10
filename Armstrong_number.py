# num = int(input("enter number"))
# for i in range(1,len(num)+1):
#     num%100     153
#     print(num)


# num = int(input("Enter a number: "))  
# sum_digits = 0

# while num > 0: 
#      (sum_digits) += num % 10**3  
#      num //= 10 
# if num==sum_digits:
#     print("it is armstrong number ")
# print("Sum of digits:", sum_digits)

num = int(input("Enter a number: "))  # Take input
original_num = num  # Store original number
sum_digits = 0  # Initialize sum

num_digits = len(str(num))  # Count the number of digits

while num > 0:
    digit = num % 10  # Extract last digit
    sum_digits += digit ** num_digits  # Raise it to the power of total digits
    num //= 10  # Remove last digit

# Check if the sum is equal to the original number
if original_num == sum_digits:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is NOT an Armstrong number.")
