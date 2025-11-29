########################################################
# Task A9_T5
# Developer Your_First_Name Your_Last_Name
# Date 2025-11-29
########################################################

print("Program starting.")

try:
    # Collecting input values
    r = input("Insert red: ")
    g = input("Insert green: ")
    b = input("Insert blue: ")

    # Convert to integers
    r = int(r)
    g = int(g)
    b = int(b)

    # Check if values are in range 0-255
    if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
        raise ValueError("Value out of range")

    # Display RGB details
    print("RGB Details:")
    print(f"- Red {r}")
    print(f"- Green {g}")
    print(f"- Blue {b}")
    print(f"- Hex #{r:02x}{g:02x}{b:02x}")
    print(f"- R-byte(base-2) {r:08b}")
    print(f"- G-byte(base-2) {g:08b}")
    print(f"- B-byte(base-2) {b:08b}")

except:
    print("Couldn't perform the designed task due to the invalid input values.")

print("Program ending.")
