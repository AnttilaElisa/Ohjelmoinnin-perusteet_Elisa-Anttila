#Create a Python program with two functions:

#main-function
#Does the routines ("Program starting." and "Program ending.")
#Utilizes askName-function.
#Utilizes greetUser-function.
#Returns None
#askName-function
#Prompts the user to insert name
#Returns name
#greetUser-function
#Which takes PName as an argument
#Greets the user "Hello {PName}!"
#Returns None
#Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.

#run 1
#Program starting.
#Insert name: John
#Hello John!
#Program ending.

def main():
    print("Program starting.")
    Pname = askName()
    greetUser(Pname)
    print("Program ending.")
    return None

def askName():
    Pname = input("Insert name: ")
    return Pname

def greetUser(Pname):
    print(f"Hello {Pname}!")
    return None

if __name__== "__main__":
    main()