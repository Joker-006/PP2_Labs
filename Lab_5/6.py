import re

# Function to replace space, comma, or dot with a colon
def replace_with_colon(text):
      # Regular expression to match space, comma, or dot
      pattern = r'[ ,.]'
      
      # Replace all occurrences with a colon
      modified_text = re.sub(pattern, ':', text)
      
      return modified_text

# Example text
text = "Hello, world. How are you today?"

# Replace spaces, commas, and dots with colons
modified_text = replace_with_colon(text)
print("Modified text:", modified_text)