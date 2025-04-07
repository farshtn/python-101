# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.

# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.

player_name = input("Please enter your name: ")
print("Hello "+ player_name + "!\nand welcome to the Shadow Lands!")
print("you walk into a creepy tomb. there are two doors, both rotten and discolored.")
sword_taken = False
while True:
    user_input = input("do you choose the left door or the right door? ")
    if user_input == "left".casefold():
        user_input = input("you enter the room it looks empty.\ngo back/look around: ")
        if user_input == "look around".casefold() and sword_taken==False:
            user_input = input("you find a sword.\ntake it/leave it: ")
            if user_input =="take it".casefold():
                print("you take the sword and leave the room and go back to the main room.")
                sword_taken = True
                continue
            elif user_input =="leave it".casefold():
                print("you leave the room without taking the sword.")
                continue
        elif user_input == "look around".casefold() and sword_taken==True:
            print("you find nothing else. you go back to the main room.")
            continue
        elif user_input == "go back".casefold():
            print("you go back to the main room.")
            continue
    elif user_input == "right".casefold():
        user_input = input("you encounter a silver scale dragon!\ngo back/FIGHT: ")
        if user_input=="fight".casefold():
            if sword_taken == True:
                print("You masterfully slay the ancient dragon!\nCongratulations "+player_name+"!\nyou leave the tomb with riches beyond your wildest imaginations!")
                break
            elif sword_taken == False:
                print("You lunge towards the ancient beast with your bare fists but...\nyou become it's food before you even know it!\nGAME OVER")
                break
        elif user_input == "go back".casefold():
            print("you go back to the main room.")
            continue
