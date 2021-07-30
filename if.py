# age = int(input("enter your age: "))
# print("you are " , age , "so.....")
#
# if age >18:
#     print("you are allowed to vote")
#
# elif age < 10:
#     print("are you insane?")
#
# else:
#     print("come back when you are eligible")
# num=3
# guess = int(input("guess the number: "))

# if num>guess:
#     print("guess higher")
#     guess = int(input("guess again: "))
#     if num==guess:
#         print("youre right")
#     else:
#         print("out of chances")
# elif num<guess:
#     print("guess lower")
#     guess = int(input("guess again: "))
#     if num==guess:
#         print("you got it")
#     else:
#         print("out of chances")
#
# else:
#     print("you got it right in first chance")

import  random
guess = random.randint(1,11)
print(guess)

num=int(input("guess the number between 1 and 10: "))

if num==guess:
    print("you are right")

else:
    if num > guess:
        print("guess lower")
    else:
        print("guess higher")
    num = int(input())
    if num == guess:
        print("right")
    else:
        print("out of choices")
