with open('text_file.txt', 'r') as file:
    # Read the entire file content
    content = file.read()
    word_counter_dict = dict()
    for word in content.split():
        clean_word = str()
        for alphabet in word:
            if alphabet.isalpha():
                clean_word += alphabet
        if clean_word in word_counter_dict:
            word_counter_dict[clean_word] +=1
        else:
            word_counter_dict[clean_word] = 1
    word_counter_dict = sorted(word_counter_dict.items())
    word_counter_dict.sort(key=lambda x: x[1], reverse=True)
    print(word_counter_dict[:5])

