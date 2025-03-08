# Function to check if a string is a palindrome
def is_palindrome(input_string):
      # Remove spaces and convert to lowercase to make the check case-insensitive
      sanitized_string=input_string.replace(" ","").lower()
      
      # Compare the string with its reverse
      return sanitized_string==sanitized_string[::-1]

# Accept input string from the user
input_string=input("Enter a string: ")

# Call the function and check if the string is a palindrome
if is_palindrome(input_string):
      print(f"'{input_string}' is a palindrome.")
else:
      print(f"'{input_string}' is not a palindrome.")