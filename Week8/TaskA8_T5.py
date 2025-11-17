from loginLib import register, login, viewProfile, change_password

def main() -> None:
    print("Program starting.")

    while True:
        showMainMenu()
        choice = int(input("Your choice: "))

        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:  # Login
            username = input("Insert username: ")
            password = input("Insert password: ")
            if login(username, password):
                print("Authentication successful!\n")
                userMenu(username)
            else:
                print("Authentication failed!\n")
        elif choice == 2:  # Register
            username = input("Insert username: ")
            password = input("Insert password: ")
            register(username, password)
            print("User registration completed!\n")
        else:
            print("Invalid choice!\n")

    print("Program ending.")

def showMainMenu() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def userMenu(username: str) -> None:
    while True:
        print("User menu:")
        print("1 - View profile")
        print("2 - Change password")
        print("0 - Logout")
        choice = int(input("Your choice: "))

        if choice == 0:
            print("Logging out...\n")
            break
        elif choice == 1:
            profile = viewProfile(username)
            if profile:
                print(f"Profile ID {profile[0]} - {profile[1]}\n")
            else:
                print("Profile not found.\n")
        elif choice == 2:
            new_pass = input("Insert new password: ")
            change_password(username, new_pass)
            print("Password changed successfully!\n")
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
