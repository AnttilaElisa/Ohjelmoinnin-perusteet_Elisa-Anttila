DELIMITER = ','


def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)


def analyseWords(words_str):
    if not words_str:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return

    words = words_str.split(DELIMITER)
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    avg_length = char_count / word_count

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))


def main():
    print("Program starting.")
    words_collected = collectWords()
    analyseWords(words_collected)
    print("Program ending.")


if __name__ == "__main__":
    main()