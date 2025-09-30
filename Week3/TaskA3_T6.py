print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = int(input("Your choice: "))

if (choice == 1):
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice2 = int(input("Your choice: "))
    
    if choice2 == 1:
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{round(meters, 1)} m is {round(kilometers, 1)} km")
    elif choice2 == 2:
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{round(kilometers, 1)} km is {round(meters, 1)} m")
    elif choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif (choice == 2):
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice2 = int(input("Your choice: "))
    
    if (choice2 == 1):
        grams = float(input("Insert grams: "))
        pounds = grams * 0.00220462
        print(f"{round(grams, 1)} g is {round(pounds, 1)} lb")
    elif choice2 == 2:
        pounds = float(input("Insert pounds: "))
        grams = pounds / 0.00220462
        print(f"{round(pounds, 1)} lb is {round(grams, 1)} g")
    elif choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == 0:
    print("\nExiting...")

else:
    print("Unknown option.")

print("\nProgram ending.")
