# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

count = 0
user_input = input("enter a string: ")
for char in user_input:
    if char in "aioue":
        count += 1
print(count)