#Datasets
#A6_T1_D1.txt
#A6_T1_D2.txt
#A6_T1_D3.txt
#Create a program that can read a text file and then print the file content. User must be able to specify the file name. Decorate the beginning and the end of the file with a decorative line.

#Decorative lines

# #### START "{filename}" ####
# #### END "{filename}" ####
#Example program runs

#run 1
#Program starting.
#This program can read a file.
#Insert filename: A6_T1_D1.txt
# #### START "A6_T1_D1.txt" ####
#Hello
#World

# #### END "A6_T1_D1.txt" ####
#Program ending.

print("Program starting.")
print("This program can read a file.")

filename = input("Insert filename: ")

file = open(filename, "r")
print(f'#### START "{filename}" ####')
content = file.read()
print(content)

file.close()
print(f'\n#### END "{filename}" ####')
print("Program ending.")
