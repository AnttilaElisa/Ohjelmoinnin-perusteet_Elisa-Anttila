#A3_T2 String comparisons
#Make Python program which does the following steps:

#Prompt user to insert
#A word
#A character
#Find if the character exists in the word. Possible prints below.
#Word "{WordFirst}" contains character "{Character}"
#Word "{WordFirst}" doesn't contain character "{Character}"
#Prompt user to insert one more word
#Compare the first word to the second word. Examples below:
#The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
#The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
#Both inserted words are the same alphabetically, "{WordFirst}"

#Example program run

#Program starting.
print("Program starting.")
#String comparisons
print("String comparisons")
#Insert first word: computer
Word = input("Insert first word: ")
#Insert a character: i
Char = input("Insert a character: ")
#Word "computer" doesn't contain character "i"
if(Char in Word):
    print(f"Word \"{Word}\" contains character \"{Char}\"")
else:
    print(f"Word \"{Word}\" doesn't contain character \"{Char}\"")
#Insert second word: computer
Word2 = input("Insert a second word: ")
#Both inserted words are the same alphabetically, "computer"
if(Word < Word2):
    print(f"The first word \"{Word}\" is before the second word \"{Word2}\", alphabetically.")
elif(Word2 < Word):
    print(f"The second word \"{Word2}\" is before the fisrt word \"{Word}\", alphabetically.")
else:
    print(f"Both inserted words are the same alphabetically, \"{Word}\"")
#Program ending.
print("Program ending.")
