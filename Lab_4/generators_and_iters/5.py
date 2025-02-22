def countdown(n):
      while n >= 0:
            yield n
            n = n - 1

n = int(input("Enter a number (N): "))

for num in countdown(n):
      print(num, end=' ')