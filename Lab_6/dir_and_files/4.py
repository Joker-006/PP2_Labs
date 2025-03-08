# Function to count the number of lines in a file
def count_lines_in_file(filename):
      with open(filename,'r') as file:
            # Read all lines and count them
            lines=file.readlines()
            return len(lines)

# Specify the file name
filename='test.txt'

# Get the line count and print the result
try:
      line_count=count_lines_in_file(filename)
      print(f"The number of lines in '{filename}' is: {line_count}")
except FileNotFoundError:
      print(f"The file '{filename}' does not exist.")