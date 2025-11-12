def main():
    print("Program starting.")
    print("Collect positive integers.")
    
    numbers: list[int] = []
    
    while True:
        try:
            user_input = int(input("Insert positive integer (negative stops): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        if user_input < 0:
            print("Stopped collecting positive integers.")
            break
        elif user_input == 0:
            print("Zero is not a positive integer. Try again.")
        else:
            numbers.append(user_input)
    
    if len(numbers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for index, value in enumerate(numbers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")
    
    print("Program ending.")


if __name__ == "__main__":
    main()
