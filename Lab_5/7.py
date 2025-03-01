def snake_to_camel(snake_str):
      # Split the snake_case string by underscores
      words = snake_str.split('_')
      
      # Convert all words except the first one to title case (capitalize first letter)
      # Join them all back together, with the first word staying in lowercase
      camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])
      
      return camel_case_str

# Test case
snake_case_string = "this_is_a_snake_case_string"
camel_case_string = snake_to_camel(snake_case_string)

print("Camel Case:", camel_case_string)