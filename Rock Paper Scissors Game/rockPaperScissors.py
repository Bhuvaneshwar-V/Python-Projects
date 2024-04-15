import random

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper and 2 for Scissors"))

if user_choice > 2 and user_choice < 0:
    print("You entered an invalid number")

else:
    computer_choice = random.randint(0, 2)

    print("Computer choose:", computer_choice)

    if computer_choice == user_choice:
        print("It's a draw")

    elif computer_choice == 0 and user_choice == 2:
        print("You lose..😔")

    elif user_choice == 0 and computer_choice == 2:
        print("You won!!✌️")

    elif computer_choice > user_choice:
        print("You lose..😔")

    elif user_choice > computer_choice:
        print("You won!!✌️")




