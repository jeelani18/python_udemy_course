for i in range(1, 10):
    print('no. {0} square is {1} and cubed is {2}'.format(i, i ** 2, i ** 3))

print()

for i in range(1, 10):
    print('no. {0} square is {1:2} and cubed is {2:3}'.format(i, i ** 2, i ** 3))#band widtth

print()

for i in range(1, 10):
    print('no. {0} square is {1:<2} and cubed is {2:<3}'.format(i, i ** 2, i ** 3))

print()

for i in range(1, 10):
    print('no. {0} square is {1:^2} and cubed is {2:^3}'.format(i, i ** 2, i ** 3))#mid align

print()

print("pi value is {0:21.21f}".format(22/7))#first is band width and second is digits we want after decimal
print("pi value is {0:21.50f}".format(22/7))
print("pi value is {0:52.50f}".format(22/7))#f gives default 6 digits after decimal
print("pi value is {0:<211.50f}".format(22/7))
print("pi value is {0:<211.54f}".format(22/7))#left align

print(f"pi value is {22/7:21.20f}")#f strings

