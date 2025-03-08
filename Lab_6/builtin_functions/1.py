from functools import reduce

# Function to multiply all numbers in the list
def multiply_all(numbers):
    return reduce(lambda x,y: x*y,numbers)

# Example list of numbers
numbers=[1,2,3,4,5]

# Call the function and print the result
result = multiply_all(numbers)
print("The product of all numbers in the list is:",result)