import re

# Function to check if the string matches the pattern
def match_string(s):
      # Regular expression to match 'a' followed by exactly two or three 'b's
      pattern = r"ab{2,3}"
      
      # Check if the entire string matches the pattern
      if re.fullmatch(pattern, s):
            return True
      return False

# Test cases
test_strings = ["ab", "abb", "abbb", "a", "abbbb", "ba", "aabb", "abbbb"]

for s in test_strings:
      if match_string(s):
            print(f"'{s}' matches the pattern.")
      else:
            print(f"'{s}' does not match the pattern.")