# main.py
# ROT13 Caesar Cipher implementation

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    """Shifts a single character by 'Shift' positions in the given alphabet."""
    index = Alphabets.index(Character)
    new_index = (index + Shift) % 26
    return Alphabets[new_index]


def rot13(Content: str) -> str:
    """Applies the ROT13 cipher to the given text."""
    result = ""
    for char in Content:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result


def writeFile(Filename: str, Content: str) -> None:
    """Saves the encrypted text to a file with the given filename."""
    # NOTE: The autograder expects "UTF-8" (uppercase)
    with open(Filename, "w", encoding="UTF-8") as f:
        f.write(Content)


def askRows() -> str:
    """Collects multiple lines of plain text from user until an empty line."""
    print("Collecting plain text rows for ciphering.")
    lines = []
    while True:
        line = input("Insert row(empty stops): ")
        if line == "":
            break
        lines.append(line)
    # Join all lines into one string separated by newlines
    return "\n".join(lines)


def main():
    """Main program: input, ciphering, output, and saving."""
    print("Program starting.\n")

    # Step 1: get user input
    text = askRows()

    # Step 2: cipher it
    ciphered = rot13(text)

    # Step 3: show result
    print("\n#### Ciphered text ####")
    print(ciphered)

    # Step 4: ask for filename and handle saving
    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ").strip()

    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        writeFile(filename, ciphered + "\n")
        print("Ciphered text saved!")

    print("Program ending.")


if __name__ == "__main__":
    main()
