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
        get_word = get_word_to_guess()
        #print(get_word)

        def new_strings(get_word):
            return list(get_word)
        split_list = new_strings(get_word)
        new_list = [ "_" for character in split_list]
        print(f"\n {new_list}\n")
        guesses = []
        number_of_guess = 8
        while number_of_guess > 0:
            if new_list != split_list:
                guess = user_guess()
                guesses.append(guess)
                if guess not in split_list:
                    number_of_guess -= 1
                else:
                    new_list = [ character if character in guesses else "_" for character in split_list]
                print(f"\nYou have {number_of_guess} guesses remaining \n {new_list} \n")
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