import random
secret_number = random.randint(1, 100)
guess = None
print("I'm thinking of a number between 1 and 100.")
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"BINGO! You got it. The number was {secret_number}.")
            
    except ValueError:
        print("Please enter a valid whole number.")
