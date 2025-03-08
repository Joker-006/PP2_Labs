import time
import math

# Function to compute the square root after a delay
def delayed_square_root(number,delay_ms):
      # Convert milliseconds to seconds
      delay_seconds=delay_ms/1000.0
      
      # Wait for the specified time in seconds
      time.sleep(delay_seconds)
      
      # Calculate the square root of the number
      result=math.sqrt(number)
      
      # Return the result
      return result

# Input
print("Sample Input:")
number=int(input())
delay_ms=int(input())

# Call the function
result=delayed_square_root(number,delay_ms)

# Output the result
print("Sample Output:")
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")