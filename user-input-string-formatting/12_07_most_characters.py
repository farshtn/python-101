# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

first_str = input("enter the 1st string: ")
second_str = input("enter the 2nd string: ")
third_str = input("enter the 3rd string: ")

if len(first_str) > len(second_str) and len(first_str) > len(third_str):
    print(first_str +"\n"+ str(len(first_str)))

elif len(second_str) > len(first_str) and len(second_str) > len(third_str):
    print(second_str +"\n"+ str(len(second_str)))

elif len(third_str) > len(second_str) and len(third_str) > len(first_str):
    print(third_str +"\n"+ str(len(third_str)))
