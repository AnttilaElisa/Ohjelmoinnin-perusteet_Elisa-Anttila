def main():
    print("Program starting.")
    
    user_input = input("Insert comma separated integers: ")

    parts = user_input.split(",")
    
    valid_integers = []
    
    for part in parts:
        part = part.strip()
        if part == "":
            continue
        try:
            number = int(part)
            valid_integers.append(number)
        except ValueError:
            print(f"Invalid value '{part}' detected.")
    
    if len(valid_integers) == 0:
        print("No values to analyse.")
        print("Program ending.")
        return
    
    total = sum(valid_integers)
    count = len(valid_integers)

    if total % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {total} and it's {parity}")
    
    print("Program ending.")


if __name__ == "__main__":
    main()
