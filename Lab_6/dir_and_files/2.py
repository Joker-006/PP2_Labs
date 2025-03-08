import os

# Function to check access to the specified path
def check_access(path):
      # Check if the path exists
      if os.path.exists(path):
            print(f"The path '{path}' exists.")

            # Check if the path is readable
            if os.access(path,os.R_OK):
                  print(f"The path '{path}' is readable.")
            else:
                  print(f"The path '{path}' is not readable.")

            # Check if the path is writable
            if os.access(path,os.W_OK):
                  print(f"The path '{path}' is writable.")
            else:
                  print(f"The path '{path}' is not writable.")

            # Check if the path is executable
            if os.access(path,os.X_OK):
                  print(f"The path '{path}' is executable.")
            else:
                  print(f"The path '{path}' is not executable.")
      else:
            print(f"The path '{path}' does not exist.")

# Specify the path to check
path='path_to_your_file_or_directory'

# Call the function to check access
check_access(path)