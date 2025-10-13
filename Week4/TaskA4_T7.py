
#Example program runs

#run 1 run 2 run 3 run 4
#Program starting.
print("Program starting.\n")

print("Check multiplicative persistence.")
num = input("Insert an integer: ")

steps = 0

while len(num) > 1:
    digits = [int(d) for d in num]
    result = 1
    for d in digits:
        result *= d
    print(" * ".join(num), "=", result)
    num = str(result)
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")
#Check multiplicative persistence.
#Insert an integer: 277777788888899
#2 * 7 * 7 * 7 * 7 * 7 * 7 * 8 * 8 * 8 * 8 * 8 * 8 * 9 * 9 = 4996238671872
#4 * 9 * 9 * 6 * 2 * 3 * 8 * 6 * 7 * 1 * 8 * 7 * 2 = 438939648
#4 * 3 * 8 * 9 * 3 * 9 * 6 * 4 * 8 = 4478976
#4 * 4 * 7 * 8 * 9 * 7 * 6 = 338688
#3 * 3 * 8 * 6 * 8 * 8 = 27648
#2 * 7 * 6 * 4 * 8 = 2688
#2 * 6 * 8 * 8 = 768
#7 * 6 * 8 = 336
#3 * 3 * 6 = 54
#5 * 4 = 20
#2 * 0 = 0
#No more steps.

#This program took 11 step(s)

#Program ending.
