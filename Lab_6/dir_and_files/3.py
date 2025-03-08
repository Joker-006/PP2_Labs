import os

# Function to check if the path exists and find filename and directory portion
def check_path(path):
      # Check if the path exists
      if os.path.exists(path):
            # If the path exists, find the filename and directory portion
            filename=os.path.basename(path)
            directory=os.path.dirname(path)

            print(f"Path exists: {path}")
            print(f"Filename: {filename}")
            print(f"Directory: {directory}")
      else:
            print(f"The path '{path}' does not exist.")

# Specify the path to check
path='path_to_your_file_or_directory'

# Call the function to check the path
check_path(path)