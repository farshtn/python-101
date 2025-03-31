# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

print(word[1:3] + word[-1] + word[-2:-7:-2] + word[-1] + word[0:1] + word[-3:-2] + word[3:-1:2])
