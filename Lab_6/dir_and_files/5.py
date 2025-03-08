# List to write to the file
my_list=["apple","banana","cherry","date","elderberry"]

# Open a file in write mode
with open("output.txt","w") as file:
      # Write each item in the list to the file, each on a new line
      for item in my_list:
            file.write(item+"\n")

print("List has been written to 'output.txt'.")