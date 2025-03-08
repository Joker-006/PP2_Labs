# Loop through the alphabet (A to Z)
for i in range(26):
      # Generate the filename (A.txt, B.txt, ..., Z.txt)
      filename=chr(65+i)+".txt"
      
      # Create and write to the text file
      with open(filename,'w') as file:
            file.write(f"This is the file {filename}")

print("26 text files (A.txt to Z.txt) have been created.")