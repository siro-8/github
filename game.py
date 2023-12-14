import random

while True:

    count = 0
    random_number = 50

    user_number = int(input("Please guess a number between 0 and 100: "))

    while True:

        if user_number < 0 or user_number > 100:
            print("Number outside of the range. Please only enter a number between 0 and 100.")
            user_number = int(input(""))
  
        elif user_number > random_number and user_number >= 0 and user_number <= 100:
            print("Too high! Try lower number. ")
            user_number = int(input(""))
            count += 1

        elif user_number < random_number and user_number >= 0 and user_number <= 100:
            print("Too low. Try higher number. ")
            user_number = int(input(""))
            count += 1

        else:
            count += 1
            print(f"Congrats! You have guessed the correct number ({random_number}). You needed {count} attemps within the 0-100 range. ")
            break

    print("-"*40)
    another_game = input("Would you like to play again? (y/n): ").lower()  

    while another_game not in ["y", "n"]:
        print("Invalid option. Please type y or n. \n")
        another_game = input("Would you like to play again? (y/n): ")
        
    if another_game == "y":
        print("Great, let's play again! \n")

    elif another_game == "n":
        print("Thanks for playing!")
        print("-"*40)
        break    