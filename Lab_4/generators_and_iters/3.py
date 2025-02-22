def divisible_by_3_and_4(start, n):
    for i in range(start, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Input values
start = int(input("Enter the starting number: "))
n = int(input("Enter the ending number: "))

# Generate numbers divisible by 3 and 4
divisible_numbers = divisible_by_3_and_4(start, n)

# Print the result
for num in divisible_numbers:
    print(num, end=' ')