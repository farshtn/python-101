# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

number = random.randrange(1,11)
print(number)
for i in range(6,0,-1):
    i -= 1
    print(f"tries left: {i}")
    if i == 0:
        print("sorry! no more tries!")
        break
    player_input = input("guess my number. it's between 1 and 10: ")
    if int(player_input) == number:
        print("congrats!")
        break
