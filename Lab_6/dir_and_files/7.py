import shutil

# Specify the source and destination file names
source_file='source.txt'
destination_file='destination.txt'

# Copy the contents from source to destination
try:
      shutil.copy(source_file, destination_file)
      print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
except FileNotFoundError:
      print(f"The file '{source_file}' does not exist.")