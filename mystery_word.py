import random


def get_word_to_guess():
    with open("words.txt") as open_file:
        read_file = open_file.read()
    new_word = read_file.split()
    string_word = random.choice(new_word)
    print(string_word)
    return string_word


def user_guess():
    user_inpt = input("Guess a letter: ")
    if len(user_inpt) == 1 and user_inpt.isalpha():
        letter = user_inpt.lower()
        #print(f"You guessed: {letter}")
        return letter
    else:
        print("\nThat guess was not a letter.\n")
        return user_guess()


def play_game():
    while True:
        get_word = "getup"
        #print(get_word)

        def new_strings(get_word):
            return list(get_word)
        string_list = new_strings(get_word)
        split_list = string_list
        new_list = [(character.replace(character, "_")) for character in split_list]
        print(f"\n {new_list}\n")
        guess = []
        while len(guess) <= 7:
            if guess != new_list:
                guess.append(user_guess())
                new_list = [(character.replace(character, "_")) if character not in guess else character for character in split_list]
                print(f"\nYou have {8 - len(guess)} guesses remaining \n {new_list} \n")
            else:
                print("You win!")
                play_again = input("Play agin? y/n : ")
                play_again_lower = play_again.lower()
                if play_again_lower == "n":
                    return play_game
                else:
                    break
        else:
            print(f"\nYou are out of guesses, the word was: {get_word} \n")
            play_again = input("Play agin? y/n : ")
            play_again_lower = play_again.lower()
            if play_again_lower == "n":
                break


if __name__ == "__main__":
    play_game()