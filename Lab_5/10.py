import re

# Function to convert camelCase to snake_case
def camel_to_snake(camel_str):
      # Use regular expression to replace uppercase letters with lowercase and prefix with an underscore
      snake_case_str = re.sub(r'([A-Z])', r'_\1', camel_str).lower()
      
      # Ensure the string doesn't start with an underscore (in case the string starts with an uppercase letter)
      if snake_case_str[0] == '_':
            snake_case_str = snake_case_str[1:]
      
      return snake_case_str

# Test case
camel_case_string = "camelCaseStringToSnakeCase"
snake_case_string = camel_to_snake(camel_case_string)

print("Snake Case:", snake_case_string)