def get_word_to_guess():
    open_file = open('test-word.txt')
    #print(open_file.read())
    string_word = str(open_file.read())
    #print(string_word)
    return string_word


def user_guess():
    user_inpt = input("Guess a letter: ")
    if user_inpt.isalpha():
        letter = user_inpt
        return letter
    else:
        print("That guess was not a letter.")
        return user_guess()

def play_game():
    get_word = get_word_to_guess()
    print(get_word)

    def split(get_word):
        return list(get_word)
    split_list = split(get_word)
    print(split_list)
    new_list = [(item.replace(item, "_")) for item in split_list]
    print(new_list)

    the_input = user_guess()
    print(the_input)



if __name__ == "__main__":
    play_game()