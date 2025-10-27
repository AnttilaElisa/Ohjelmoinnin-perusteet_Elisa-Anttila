#Create a menu-driven Python program with following options:

#Insert a word
#Which stores user inserted word into memory.
#Show current word
#Prints the word from the memory
#Show current word in reverse
#Prints the word from the memory in reverse.
#Exit
#Stops the program gracefully
#Unknown option
#Initialize the Word with an empty string.

#Example program runs

#run 1
#Program starting.
#Options:
#1 - Insert word
#2 - Show current word
#3 - Show current word in reverse
#0 - Exit
#Your choice: 1
#Insert word: Banana

#Options:
#1 - Insert word
#2 - Show current word
#3 - Show current word in reverse
#0 - Exit
#Your choice: 2
#Current word - "Banana"

#Options:
#1 - Insert word
#2 - Show current word
#3 - Show current word in reverse
#0 - Exit
#Your choice: 3
#Word reversed - "ananaB"

#Options:
#1 - Insert word
#2 - Show current word
#3 - Show current word in reverse
#0 - Exit
#Your choice: 0
#Exiting program.

#Program ending.

def showMenu() -> None:
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")

def insertWord():
    word = str(input("Insert word: "))
    return word

def showWord(currentWord):
    print(f'Current word - "{currentWord}"')
    return None

def showWordReversed(currentWord) -> None:
    reversedWord = currentWord[::-1]
    print(f'Word reversed - "{reversedWord}"')
    return None

def main():
    print("Program starting.")
    word = ""

    while True:
        print()
        showMenu()
        choice = input("Your choice: ")

        if choice == "1":
            word = insertWord()
        elif choice == "2":
            showWord(word)
        elif choice == "3":
            showWordReversed(word)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option, please try again.")

    print()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
