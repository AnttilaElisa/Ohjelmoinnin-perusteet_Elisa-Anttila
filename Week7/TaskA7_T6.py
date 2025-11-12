rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

seed = 1234
def fake_random_choice():
    """Return a pseudo-random number between 1 and 3 (inclusive)."""
    global seed
    seed = (seed * 7 + 5) % 10
    return (seed % 3) + 1

print("Program starting.")
print("Welcome to the rock-paper-scissors game!")

player_name = input("Insert player name: ")
print(f"Welcome {player_name}!")
print("Your opponent is RPS-3PO.")
print("Game starts...\n")

player_wins = 0
bot_wins = 0
draws = 0

choices = {1: "rock", 2: "paper", 3: "scissors"}
ascii_art = {1: rock, 2: paper, 3: scissors}

while True:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")

    try:
        player_choice = int(input("Your choice: "))
    except ValueError:
        print("Please enter a number between 0 and 3.\n")
        continue

    if player_choice == 0:
        break

    if player_choice not in [1, 2, 3]:
        print("Invalid choice. Try again.\n")
        continue

    bot_choice = fake_random_choice()

    print("Rock! Paper! Scissors! Shoot!\n")
    print("#########################")
    print(f"{player_name} chose {choices[player_choice]}.\n")
    print(ascii_art[player_choice])
    print("#########################")
    print(f"RPS-3PO chose {choices[bot_choice]}.\n")
    print(ascii_art[bot_choice])
    print("#########################\n")

    if player_choice == bot_choice:
        print(f"Draw! Both players chose {choices[player_choice]}.\n")
        draws += 1
    elif (player_choice == 1 and bot_choice == 3) or \
         (player_choice == 2 and bot_choice == 1) or \
         (player_choice == 3 and bot_choice == 2):
        print(f"{player_name}'s {choices[player_choice]} beats RPS-3PO's {choices[bot_choice]}!\n")
        player_wins += 1
    else:
        print(f"RPS-3PO's {choices[bot_choice]} beats {player_name}'s {choices[player_choice]}!\n")
        bot_wins += 1

print("\nResults:")
print(f"{player_name} - wins ({player_wins}), losses ({bot_wins}), draws ({draws})")
print(f"RPS-3PO - wins ({bot_wins}), losses ({player_wins}), draws ({draws})\n")
print("Program ending.")
