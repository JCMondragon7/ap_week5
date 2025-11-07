def manipulate_words():
    # Manipulating Words:
    #Given the string info
    # a. Extract the word 'subjective' without knowing its exact position.
    # b. Extract every third word.
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.
    #A
    quote2 = "Python is fun. Fun is good. Good is subjective."
    word_to_find = "subjective"
    start_index = quote2.find(word_to_find)
    if start_index != -1:
        extracted_word = quote2[start_index : start_index + len(word_to_find)]
        print(f"a. Extracted word: {extracted_word}")
    else:
        print(f"a. The word '{word_to_find}' was not found.")
    #make word variable
    #quote.fin word, if its found print, if not just print not found
    #B
    #c
    words_list = quote2.split() #splits words up
    words_list_reversed = words_list[::-1] #reverses words
    reversed_quote = ' '.join(words_list_reversed)
    print(f"c. Words in reverse position: {reversed_quote}")