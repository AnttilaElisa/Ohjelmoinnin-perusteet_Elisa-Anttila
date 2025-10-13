#Program starting.
print("Program starting.\n")
#Insert starting value: 1
#Insert stopping value: 10
Start = int(input("Insert starting value: "))
Stop = int(input("Insert stopping value: "))
#Starting for-loop:
print("\nStarting for-loop:")
if Start <= Stop:
    for i in range(Start, Stop + 1): 
        print(i)

#Program ending.
print("\nProgram ending.")

