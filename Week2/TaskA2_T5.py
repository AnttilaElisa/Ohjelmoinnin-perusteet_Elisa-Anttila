print("Program starting.\n")
Compound = input("Insert a closed compound word: ")
Reversed_compound = Compound[::-1]
print(f"The word you inserted is '{Compound}' and in reverse it is '{Reversed_compound}'.")
Length = (len(Compound))
print(f"The inserted word length is {Length}")
Last_char = Compound[-1]
print(f"Last character is '{Last_char}'\n")
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
substring = Compound[start:end:step]
print(f"\nThe word '{Compound}' sliced to the defined substring is '{substring}'.")
print("Program ending.")