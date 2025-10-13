print("Program starting.")
print("")
WordCount = 0
CharCount = 0

Word = input("Insert word (empty stops): ")
while Word != "":
    WordCount += 1
    CharCount += len(Word)
    Word = input("Insert word (empty stops): ")

print("")
print("You inserted:")
print(f"- {WordCount} words")
print(f"- {CharCount} words")
print("")
print("Program ending.")


#TAI

print("Program starting.\n")
WordCount = 0
CharCount = 0

while True:
    Word = input("Insert word (empty stops): ")
    if Word != "":
        break
    WordCount += 1
    CharCount += len(Word)

print("\nYou inserted:")
print(f"- {WordCount} words")
print(f"- {CharCount} words")
print("\nProgram ending.")

#TAI

DELIMETER = ","

def collectWords():
    CWords = []
    while True:
        CWord = input("Insert word(empty stops): ")
        if CWord == "":
            break
        CWords.append(CWord)
    return DELIMETER.join(CWords)

def analyseWords(PWords):
    AWords = PWords.split(DELIMETER)
    Words = len(AWords)
    Characters = sum(len(Word) for Word in AWords)
    Avg = Characters / Words
    if Characters == 0:
        print("- 0 Words")
    else:
        print(f"- {Words} Words")
    print(f"- {Characters} Characters")
    print("- {:.2f} Average word length".format[Avg])

def main():
    print("Program starting.")
    Words = collectWords()
    analyseWords(Words)
    print("Program ending.")

main()
