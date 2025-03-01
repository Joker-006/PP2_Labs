import re

# Function to insert spaces before capital letters
def insert_spaces(s):
      # Use regular expression to add space before each capital letter
      result = re.sub(r'(?<=[a-z])([A-Z])', r' \1', s)
      
      return result

# Test case
input_string = "ThisIsAStringWithCapitalLetters"
modified_string = insert_spaces(input_string)

print("Modified string:", modified_string)