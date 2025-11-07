#Create a program that copies a text file by reading from a source file and writing the content to a destination file.
#Allow the user to specify the source and destination file names.

#Example program runs

#run 1
#Program starting.
#This program can copy a file.
#Insert source filename: A6_T3_D1.txt
#Insert destination filename: A6_T3_F1.txt
#Reading file 'A6_T3_D1.txt' content.
#File content ready in memory.
#Writing content into file 'A6_T3_F1.txt'.
#Copying operation complete.
#Program ending.

print("Program starting.")
print("This program can copy a file.")
source = input("Insert source filename: ")
destination = input("Insert destination filename: ")

print(f"Reading file '{source}' content.")
s_file = open(source, "r", encoding="utf-8")
content = s_file.read()
s_file.close()
print("File content ready in memory.")

print(f"Writing content into file '{destination}'.")
d_file = open(destination, "w", encoding="utf-8")
d_file.write(content)
d_file.close()
print("Copying operation complete.")

print("Program ending.")