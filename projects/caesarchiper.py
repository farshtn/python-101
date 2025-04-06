lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7


for char in secret.lower():
    if char.isalpha():
        char_ind = lowercase_letters.find(char)
        if char_ind + cipher> 25:
            char_ind = char_ind - 26 + cipher
            ciphered_char = lowercase_letters[char_ind]
            print(ciphered_char,end="")
        else:
            char_ind += cipher
            ciphered_char = lowercase_letters[char_ind]
            print(ciphered_char,end="")
    elif char.isalpha() == False:
        print(char,end="")
        
print()