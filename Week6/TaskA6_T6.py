LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    index = Alphabets.index(Character)
    new_index = (index + Shift) % 26
    return Alphabets[new_index]


def rot13(Content: str) -> str:
    result = ""
    for char in Content:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char
    return result


def writeFile(Filename: str, Content: str) -> None:
    with open(Filename, "w", encoding="UTF-8") as f:
        f.write(Content)


def askRows() -> str:
    print("Collecting plain text rows for ciphering.")
    lines = []
    while True:
        line = input("Insert row(empty stops): ")
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    print("Program starting.\n")

    text = askRows()

    ciphered = rot13(text)

    print("\n#### Ciphered text ####")
    print(ciphered)

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

