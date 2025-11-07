print("Program starting.")

first_name = input("Insert first name: ")
last_name = input("Insert last name: ")
filename = input("Insert filename: ")

file = open(filename, "w")
file.write(first_name + "\n")
file.write(last_name + "\n") 
file.write("\n")
file.close()

print("Program ending.")

