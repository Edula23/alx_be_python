import random 
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
match guess:
    case _ if guess < secret_number:
        print("Too low!")
        guess = int(input("Try again: "))
    case _ if guess > secret_number:
        print("Too high!")
        guess = int(input("Try again: "))
    case _:
        print("Congratulations! You guessed it!")
        playAgain = input("Do you want to play again? (yes/no): ").lower()
        if playAgain == 'yes':
            secret_number = random.randint(1, 10)
            guess = int(input("Guess a number between 1 and 10: "))
        else:
            print("Thanks for playing!")
