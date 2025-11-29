########################################################
# Task A10_Tx
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################


# Program starting
print("Program starting.")

# Prompt user to insert filename
filename = input("Insert filename: ")

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read all lines, strip newlines, and ignore empty rows
        lines = [line.strip() for line in file if line.strip()]

        # Flatten all values into a single list
        values = []
        for line in lines:
            # Split line by whitespace
            values.extend(line.split())

    # --- Vertically ---
    print("# --- Vertically --- #")
    for value in values:
        print(value)
    print("# --- Vertically --- #\n")

    # --- Horizontally ---
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Program ending
print("Program ending.")