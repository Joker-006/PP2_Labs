import re

# Function to check if the string matches the pattern
def match_string(s):
      # Regular expression to match 'a' followed by anything, ending in 'b'
      pattern = r'a.*b'
      
      # Check if the entire string matches the pattern
      if re.fullmatch(pattern, s):
            return True
      return False

# Test cases
test_strings = ["ab", "acb", "a123b", "abc", "a", "b", "abbb", "xyz", "babab"]

for s in test_strings:
      if match_string(s):
            print(f"'{s}' matches the pattern.")
      else:
            print(f"'{s}' does not match the pattern.")