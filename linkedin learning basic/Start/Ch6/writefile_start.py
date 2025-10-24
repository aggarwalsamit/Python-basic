# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods

sample_file = open("textfile.txt","w+")
sample_file.write("this is some sample test in out sample file")
sample_file.close()

# Open a file for writing and create it if it doesn't exist


# Open the file for appending text to the end
sample_file = open("textfile.txt", "a+")
sample_file.write("this is some sample test in out sample file2")
sample_file.close()

# write some lines of data to the file


# close the file when done
