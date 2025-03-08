# Function to calculate the number of uppercase and lowercase letters
def count_case_letters(input_string):
      # Initialize counters
      upper_case_count=0
      lower_case_count=0
      
      # Loop through each character in the string
      for char in input_string:
            if char.isupper():
                  upper_case_count=upper_case_count+1
            elif char.islower():
                  lower_case_count=lower_case_count+1
      
      return upper_case_count,lower_case_count

# Accept input string from the user
input_string=input("Enter a string: ")

# Call the function and get the counts
upper_count,lower_count=count_case_letters(input_string)

# Print the results
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")