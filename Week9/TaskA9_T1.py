########################################################
# Task A9_T1
# Developer Your_First_Name Your_Last_Name
# Date 2025-11-29
########################################################

print("Program starting.\n")

total_sum = 0.0

while True:
    user_input = input("Insert a floating-point value (0 to stop): ")

    try:
        value = float(user_input)
    except ValueError:
        print("Error! '{}' couldn't be converted to float.".format(user_input))
        continue

    if value == 0:
        break

    total_sum += value

print("\nFinal sum is {:.2f}".format(total_sum))
print("Program ending.")
