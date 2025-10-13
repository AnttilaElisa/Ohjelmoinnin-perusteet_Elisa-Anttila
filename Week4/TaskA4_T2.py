#Copy the previous program and modify the behaviour to match the example program run below. This program must use “for-loop” structure.

#It is recommended to replace the print-command end character with space, so that all the iterations can be printed on the same row. Last iteration might require additional logic to get rid of the extra space at the end.

#Note! the autograding tool will test that the correct structure has been applied.

#Example program runs

#run 1
#Program starting.
print("Program starting.\n")

Start = int(input("Insert starting value: "))
Stop = int(input("Insert stopping value: "))
#Starting for-loop:
#1 2 3 4 5 6 7 8 9 10
print("\nStarting for-loop:")
if Start <= Stop:
    for i in range(Start, Stop + 1): 
        print(i, end=" ")

#Program ending.
print("")
print("\nProgram ending.")
