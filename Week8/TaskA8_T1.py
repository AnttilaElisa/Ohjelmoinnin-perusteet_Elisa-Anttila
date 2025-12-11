import time

def main() -> None:
    print("Program starting.")
    pause_duration = 1.0 

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            pause_duration = float(input("Insert pause duration (s): "))
        elif choice == 2:
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)
            print("Unpaused.\n")
        elif choice == 0:
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice!\n")

    print("Program ending.")


def showOptions() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


if __name__ == "__main__":
    main()

