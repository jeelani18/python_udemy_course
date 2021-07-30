sen = input("what is important for a human? ")

if "brain" in sen.casefold():
    print("you have ", sen, "you have to use it")

elif "brain" not in sen:
    print("do you use it? ")

else:
    print("not found")

print("*" * 100)

name = input("name?")
age =int(input("age?"))

if 18 < age < 31:
    print("you are welcome")

else:
    print("sry we cant allow you")