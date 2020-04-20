secret = int("5")
guess = int(input("Guess the number (hint: it's between 0-15): "))

if guess == secret:
    print("You guessed correctly!")
else:
    print("Wrong number")
