import random

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

num = random.randint(1, 10)
guess = 0
track = 0

while guess != num and guess != "exit":
    guess = input("Guess a number between 1 & 9. If you wish to end the game, please type 'exit'. Enter your number: ")

    if guess == "exit":
        print("Giving up already! Come back and try again soon.")
        break

    guess = int(guess)
    track +- 1
    if guess not in range (1, 10):
        print("Doh! Please input a number between 1 & 9.")
    elif guess < num:
        print("Too low bub.")
    elif guess > num:
        print("Shootin' too high there pal.")
    else:
        if track == 1:
            print("You got it dude! :thumbs_up:")