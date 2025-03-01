import re

# Function to check if the string matches the pattern
def match_string(s):
      # Regular expression to match 'a' followed by zero or more 'b's
      pattern = r"ab*"
    
      # Check if the entire string matches the pattern
      if re.fullmatch(pattern, s):
            return True
      return False

# Test cases
test_strings = ["a", "ab", "abb", "abbb", "b", "ba", "aabb"]

for s in test_strings:
      if match_string(s):
            print(f"'{s}' matches the pattern.")
      else:
            print(f"'{s}' does not match the pattern.")