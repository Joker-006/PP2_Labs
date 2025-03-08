import os

# Function to list only directories in the specified path
def list_directories(path):
      try:
            # List all directories
            directories=[entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path,entry))]
            print("Directories in the specified path:")
            for directory in directories:
                  print(directory)
      except FileNotFoundError:
            print(f"The path '{path}' does not exist.")
      except PermissionError:
            print(f"You do not have permission to access the path '{path}'.")

# Function to list only files in the specified path
def list_files(path):
      try:
            # List all files
            files=[entry for entry in os.listdir(path) if os.path.isfile(os.path.join(path,entry))]
            print("Files in the specified path:")
            for file in files:
                  print(file)
      except FileNotFoundError:
            print(f"The path '{path}' does not exist.")
      except PermissionError:
            print(f"You do not have permission to access the path '{path}'.")

# Function to list both directories and files in the specified path
def list_all(path):
      try:
            # List all directories and files
            all_entries=os.listdir(path)
            print("All directories and files in the specified path:")
            for entry in all_entries:
                  print(entry)
      except FileNotFoundError:
            print(f"The path '{path}' does not exist.")
      except PermissionError:
            print(f"You do not have permission to access the path '{path}'.")

# Specify the path
path='path_to_your_directory'

# Call the functions
list_directories(path)
list_files(path)
list_all(path)