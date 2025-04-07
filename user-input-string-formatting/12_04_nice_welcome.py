# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input("please enter your name: ")
second_name_index = name.index(" ")
first_name = ""
x = 0
for char in name:
    if name.index(char) < second_name_index:
        first_name += name[x]
    elif name.index(char) >= second_name_index:
        break
    x = x+1
print(f"hello dear {first_name} and welcome to my script!")