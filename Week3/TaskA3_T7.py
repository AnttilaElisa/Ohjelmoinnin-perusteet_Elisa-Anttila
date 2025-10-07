#Prompt user to insert value as an integer.
#Display menu
#option 1 - In one multi-branched decision
#option 2 - Independent if-statement decisions
#option 0 - Exit
#Prompt user to choose option
#Apply following math operations in the options 1 & 2
#One multi-branched decision structure:
#Value is 400 or more => add 44 to the existing value
#Value is 200 or more => add 22 to the existing value
#Value is 100 or more => add 11 to the existing value
#Independent if-statement decisions one after another:
#Value is 400 or more => add 44 to the existing value
#Value is 200 or more => add 22 to the existing value
#Value is 100 or more => add 11 to the existing value
#Exit: “Exiting…”
#At the end of the options 1 & 2, show the results like in the example program runs.
#Other possible output variats:

#“Unknown option.”
#Example program runs

#run 1 run 2 run 3 run 4 run 5 run 6
#Program starting.
print("Program staring.")
#Testing decision structures.
print("Testing decision structures.")
#Insert an integer: 250
Feed = input("Insert an integer: ")
Value = int(Feed)
#Options:
#1 - In one multi-branched decision
#2 - In multiple independent if-statements
#0 - Exit
print("Options:")
print("#1 - In one multi-branched decision")
print("#2 - In multiple independent if-statements")
print("#0 - Exit")
#Your choice: 1
Feed = input("Your choise: ")
Choise = int(Feed)
if(Choise == 1): 
    print("Using one multi-branched decision structure.")
    if(Value >= 400):
        #Value = Value + 44
        Value += 44
    elif(Value >= 200):
        #Value = Value + 22
        Value += 22
    elif(Value >= 100):
        #Value = Value + 11
        Value += 11
    print(f"Result is {Value}")
if(Choise == 2):
    if(Value >= 400):
        #Value = Value + 44
        Value += 44
    if(Value >= 200):
        #Value = Value + 22
        Value += 22
    if(Value >= 100):
        #Value = Value + 11
        Value += 11
    print(f"Result is {Value}")
if(Choise == 0):
    print("Exiting...")
else:
    print("Unknown option")
#Result is 272
print("")
#Program ending.
print("Program ending.")
