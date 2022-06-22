def get_word_to_guess():
    open_file = open("test-word.txt")
    #print(open_file.read())
    string_word = str(open_file.read())
    #print(string_word)
    return string_word


def user_guess():
    user_inpt = input("Guess a letter: ")
    if len(user_inpt) == 1 and user_inpt.isalpha():
        letter = user_inpt.lower()
        print(f"You guessed: {letter}")
        return letter
    else:
        print("That guess was not a letter.")
        return user_guess()


def play_game():
    while True:
        get_word = get_word_to_guess()
        #print(get_word)

        def new_strings(get_word):
            return list(get_word)
        string_list = new_strings(get_word)
        split_list = string_list
        #print(split_list[:-1])
        new_list = [(item.replace(item, "_")) for item in split_list[:-1]]
        print(new_list)
        guess = []
        while len(guess) <= 7:
            guess.append(user_guess())
            new_list = [(item.replace(item, "_")) if item not in guess else item for item in split_list[:-1]]
            print(f"You have {8 - len(guess)} guesses remaing \n {new_list} ")
        else:
            print("You are out of guesses")
        play_again = input("Play agin? y/n ")
        if play_again == "n":
            break




if __name__ == "__main__":
    play_game()