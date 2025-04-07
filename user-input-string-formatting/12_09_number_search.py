# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

digit = 0
number = int(input("enter a number between 1 and 1,000,000,000: "))
if number not in range(1,1000000001):
    print("the number is not in the specified range! please enter a number between 1 and 1,000,000,000 next time!")
else:
    while digit != number:
        digit += 1
        if digit == number:
            print(digit)
            break