low = 1
high = 100

print("think of a number between 1 and 100")
input("press enter to start")

guesses = 1

while True:

    guess = low + (high - low) // 2
    hl = input("my guess is {} , should i think higher or lower or am i correct ? answer in h or l or c ".format(guess))

    if hl == "h":
        low = guess + 1

    elif hl == "l":
        high = guess - 1

    elif hl == "c":
        print("i guessed it in {} guesses".format(guesses))
        break

    else:
        print("only enter h or l or c")

    guesses = guesses + 1
