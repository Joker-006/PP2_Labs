def generate_even_numbers(n):
    for i in range(0, n+1, 2):  # Start at 0, step by 2 to get even numbers
        yield i

# Input value
n = int(input("Enter a number: "))

# Generate even numbers using the generator
even_numbers = generate_even_numbers(n)

# Print even numbers in a comma-separated format
print(', '.join(map(str, even_numbers)))