print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = int(input("Your choice: "))
if(choice == 1):
    Celsius = float(input("Insert the amount of Celsius: "))
    Fahrenheits = Celsius * 1.8 + 32
    print(f"{round(Celsius, 1)} °C equals to {round(Fahrenheits, 1)} °F")
elif(choice == 2):
    Fahrenheits = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheits - 32) / 1.8
    print(f"{round(Fahrenheits, 1)} °F equals to {round(Celsius, 1)} °C")
elif(choice == 0):
    print("Exiting...")
else:
    print("Unknown option.")
print("")    
print("Program ending.")
