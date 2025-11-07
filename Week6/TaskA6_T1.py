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