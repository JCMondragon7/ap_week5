def advanced_slice():
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