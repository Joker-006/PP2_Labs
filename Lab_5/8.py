import re

# Function to split a string at uppercase letters
def split_at_uppercase(s):
      # Regular expression to split at each uppercase letter
      result = re.split(r'(?=[A-Z])', s)
      
      return result

# Test case
input_string = "ThisIsAStringWithUppercaseLetters"
split_string = split_at_uppercase(input_string)

print("Split string:", split_string)