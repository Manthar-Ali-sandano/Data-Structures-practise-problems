def reverse_list_recursive(input_list):
    
    if len(input_list) <= 1:
        return input_list
    
    return reverse_list_recursive(input_list[1:]) + [input_list[0]]

# Example usage
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list_recursive(my_list)
print("Original List:", my_list)
print("Reversed List (using recursion):", reversed_list)