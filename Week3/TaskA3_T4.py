# A3_T4 More menu options

print("Program: starting")
print("This is a program with simple menu, where you can choose which operation the program performs.")

# Ask for name before showing menu
name = input("Before the menu, please insert your name: ")

print("\nOptions:")
print("1 -- Print welcome message")
print("2 -- Print the name backwards")
print("3 -- Print the first character")
print("4 -- Show the amount of characters in the name")
print("0 -- Exit")

choice = int(input("Your choice: "))
print("Please enter a number between 0 and 4.")

if(choice == 1):
    print(f"Welcome {name}!")
elif(choice == 2):
    print(f"Your name backwards is \"{name[::-1]}\"")
elif(choice == 3):
    print(f"The first character in name \"{name}\" is \"{name[0]}\"")
elif(choice == 4):
    print(f"There are {len(name)} characters in the name \"{name}\"")
elif(choice == 0):
    print("Exiting program...")
else:
    print("Unknown option.")

print("\nProgram: ending")
