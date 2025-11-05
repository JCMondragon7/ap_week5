# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7: 10])
hij_index = alphabet.index('hij') # index of substring
print(hij_index) #7
# b. Extract every second letter starting from 'a' to 'm'.
every_second_leter = alphabet[0:13:2] # a is 0, m is 13, 2 is every second
print(every_second_leter)
# c. Reverse the entire string using slicing.
reverse_alphabet = alphabet[::-1] #reverses entire string as 0:0:-1
print(reverse_alphabet)

# Problem Set 2: Extracting Information
# From Descriptions:
#Extract the name of the famous personality from the 
quote1 = 'Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy'
    #personality_name = quote.spit('-')[-1].strip() # this is messy
print(quote1.find('John F. Kennedy')) #78

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


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
phrase = "MAY THE FORCE BE WITH YOU."

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
mottos = ["Make", "haste", "slowly."]
separator = " "
result_string = separator.join(mottos)
print(result_string)

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
letter_to_count = 'i'
