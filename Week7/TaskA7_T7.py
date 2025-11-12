alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

configs = {
    "iconf1.txt": {
        "rotors": [
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ],
        "reflector": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    },
    "iconf2.txt": {
        "rotors": [
            "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        ],
        "reflector": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    },
    "iconf3.txt": {
        "rotors": [
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        ],
        "reflector": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    }
}

def forward_pass(letter, rotor, position):
    index = (alphabet.index(letter) + position) % 26
    mapped = rotor[index]
    return alphabet[(alphabet.index(mapped) - position) % 26]

def backward_pass(letter, rotor, position):
    index = (alphabet.index(letter) + position) % 26
    mapped_index = rotor.index(alphabet[index])
    return alphabet[(mapped_index - position) % 26]

def run_enigma():
    config_file = input("Insert config(filename): ").strip()

    if config_file not in configs:
        print("Invalid config filename.")
        return

    plugs = input("Insert plugs (y/n)?: ").strip().lower()
    print("No extra plugs inserted.")
    print("Enigma initialized.\n")

    rotors = configs[config_file]["rotors"]
    reflector = configs[config_file]["reflector"]

    while True:
        row = input("Insert row (empty stops): ").upper()
        if row == "":
            print("\nEnigma closing.")
            break

        rotor_positions = [0, 0, 0]
        output = ""

        for ch in row:
            if ch not in alphabet:
                output += ch
                print(f'Character "{ch}" illuminated as "{ch}"')
                continue

            rotor_positions[0] = (rotor_positions[0] + 1) % 26
            if rotor_positions[0] == 0:
                rotor_positions[1] = (rotor_positions[1] + 1) % 26
            if rotor_positions[1] == 0 and rotor_positions[0] == 0:
                rotor_positions[2] = (rotor_positions[2] + 1) % 26

            letter = ch
            for i in range(3):
                letter = forward_pass(letter, rotors[i], rotor_positions[i])

            letter = reflector[alphabet.index(letter)]

            for i in reversed(range(3)):
                letter = backward_pass(letter, rotors[i], rotor_positions[i])

            print(f'Character "{ch}" illuminated as "{letter}"')
            output += letter

        print(f'Converted row - "{output}".\n')

if __name__ == "__main__":
    print("Welcome to the Enigma Machine Simulation!")
    run_enigma()
