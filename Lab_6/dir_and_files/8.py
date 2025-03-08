import os

# Function to delete a file after checking if it exists and if access is allowed
def delete_file(file_path):
      # Check if the file exists
      if os.path.exists(file_path):
            # Check if the file is accessible (can be deleted)
            if os.access(file_path,os.W_OK):  # os.W_OK checks if the file is writable (deletable)
                  try:
                        # Delete the file
                        os.remove(file_path)
                        print(f"File '{file_path}' has been deleted.")
                  except Exception as e:
                        print(f"An error occurred while deleting the file: {e}")
            else:
                  print(f"You do not have permission to delete the file '{file_path}'.")
      else:
            print(f"The file '{file_path}' does not exist.")

# Specify the file path
file_path = 'path_to_your_file.txt'

# Call the function to delete the file
delete_file(file_path)