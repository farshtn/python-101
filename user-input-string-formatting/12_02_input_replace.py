# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

sentence = input("please write a sentence: ")
symbol = input("please write symbol: ")
sentence_first_letter = sentence[0]
for char in sentence:
    if char == sentence[0]:
        print(symbol,end="")
    else:
        print(char,end="")
print()