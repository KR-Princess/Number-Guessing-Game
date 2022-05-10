import random

print("NUMBER GUESSING GAME")
print("Guess a number between 1 and 10")

chances = 5
number= random.randint(1,10)
# While loop to count the number of chances remaining
while chances >= 1:
    guess = int(input("Enter your guess! "))
    # int means integer

    if guess == number:
        # If the number entered by the user is the same as the computer generated number, then break from loop using loop control statement 'break'
        print("Congratulations, YOU WON!")
        break
    elif guess < number:
        print("Your guess was too low. Enter a number higher than ", guess)
    else:
        print("Your guess was too high. Enter a number lower than", guess)

    chances= chances-1

if chances==0:
    print("You LOSE! The number is",  number)