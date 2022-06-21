def play_game():
    open_file = open('test-word.txt')
    #print(open_file.read())
    string_word = str(open_file.read())
    #print(string_word)
    
    def split(string_word):
        return list(string_word)
    split_list = split(string_word)
    print(split_list)
    new_list = [(item.replace(item, "_")) for item in split_list]
    print(new_list)



if __name__ == "__main__":
    play_game()