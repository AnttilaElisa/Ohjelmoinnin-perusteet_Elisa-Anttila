LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13(text: str) -> str:
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            result += LOWER_ALPHABETS[(LOWER_ALPHABETS.index(char) + 13) % 26]
        elif char in UPPER_ALPHABETS:
            result += UPPER_ALPHABETS[(UPPER_ALPHABETS.index(char) + 13) % 26]
        else:
            result += char
    return result


def read_progress(filename: str = "player_progress.txt") -> list[str]:
    with open(filename, "r", encoding="UTF-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def append_to_progress(content: str, filename: str = "player_progress.txt") -> None:
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(content + "\n")


def read_message_file(next_id: str, passphrase: str) -> list[str]:
    filename = f"{next_id}_{passphrase}.gkg"
    with open(filename, "r", encoding="UTF-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def save_plain_message(next_id: str, plain_passphrase: str, plain_message: str) -> None:
    filename = f"{next_id}-{plain_passphrase}.txt"
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(plain_message + "\n")


def travel():
    print("Travel starting.")

    progress_lines = read_progress()
    last_row = progress_lines[-1]
    current_id, next_id, passphrase_cipher = last_row.split(";")

    locations = {
        "0": "home",
        "1": "Galba's palace",
        "2": "Otho's palace",
        "3": "Vitellius' palace",
        "4": "Vespasian's palace"
    }

    print(f"Currently at {locations.get(current_id, 'unknown location')}.")
    print(f"Travelling to {locations.get(next_id, 'unknown destination')}...")
    print(f"...Arriving to the {locations.get(next_id, 'unknown destination')}.")
    print("Passing the guard at the entrance.")

    plain_passphrase = rot13(passphrase_cipher)
    print(f"\"{plain_passphrase.capitalize()}!\"")

    print("Looking for the message in the palace...")
    lines = read_message_file(next_id, passphrase_cipher)

    print("Ah, there it is! Seems cryptic.")
    append_to_progress(lines[0])
    print("[Game] Progress autosaved!")

    print("Deciphering Emperor's message...")
    ciphered_message = "\n".join(lines[1:])
    plain_message = rot13(ciphered_message)

    save_plain_message(next_id, plain_passphrase, plain_message)
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")


def main():
    travel()


if __name__ == "__main__":
    main()
