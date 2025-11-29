########################################################
# Task A9_T6
# Developer Your_First_Name Your_Last_Name
# Date 2025-11-29
########################################################

lines = []

print("Program starting.")

try:
    while True:
        # Display menu
        print("\nOptions:")
        print("1 - Insert line")
        print("2 - Save lines")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            text = input("Insert text: ")
            lines.append(text)

        elif choice == "2":
            if not lines:
                print("No lines to save.")
            else:
                filename = input("Insert filename: ")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines))
                print(f"{len(lines)} lines saved to {filename}.")

        elif choice == "0":
            if lines:
                save_choice = input("You have unsaved lines. Save before quit(y/n)?: ").strip().lower()
                if save_choice == "y":
                    filename = input("Insert filename: ")
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write("\n".join(lines))
                    print(f"{len(lines)} lines saved to {filename}.")
            break

        else:
            print("Invalid choice, try again.")

except KeyboardInterrupt:
    print("\nKeyboard interrupt and unsaved progress!")
    if lines:
        save_choice = input("Save before quit(y/n)?: ").strip().lower()
        if save_choice == "y":
            filename = input("Insert filename: ")
            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print(f"{len(lines)} lines saved to {filename}.")

print("Program ending.")
