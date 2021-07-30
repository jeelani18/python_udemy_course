import random
guess = random.randint(1,10)
print(guess)
num = int(input("guess number between 1 and 10: "))

while num!=guess:
    num =int(input("guess again"))

    if num == guess:
        print('right')
        break
    else:
        if num > guess:
            print('guess lower')
        else:
            print('guess higher')
