import re

# Function to find sequences of lowercase letters joined with underscores
def find_sequences(text):
      # Regular expression to find sequences of lowercase letters joined with underscores
      pattern = r'[a-z]+(_[a-z]+)*'
      
      # Find all sequences matching the pattern
      matches = re.findall(pattern, text)
      
      return matches

# Example text
text = "this_is_a_test string_with_multiple_parts test_case and_example not_a_match example_1"

# Find and print sequences of lowercase letters joined with underscores
sequences = find_sequences(text)
print("Sequences of lowercase letters joined with underscores:", sequences)