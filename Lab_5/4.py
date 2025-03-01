import re

# Function to find sequences of one uppercase letter followed by lowercase letters
def find_sequences(text):
      # Regular expression to find sequences of an uppercase letter followed by lowercase letters
      pattern = r'[A-Z][a-z]+'
      
      # Find all sequences matching the pattern
      matches = re.findall(pattern, text)
      
      return matches

# Example text
text = "Hello world! This is a TestString example for FindingPatterns."

# Find and print sequences of an uppercase letter followed by lowercase letters
sequences = find_sequences(text)
print("Sequences of uppercase followed by lowercase letters:", sequences)