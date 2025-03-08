# Function to check if all elements of a tuple are true
def all_elements_true(input_tuple):
      return all(input_tuple)

# Example tuple
input_tuple=(1,2,3,4,5)

# Call the function and print the result
if all_elements_true(input_tuple):
      print("All elements in the tuple are True.")
else:
      print("Not all elements in the tuple are True.")