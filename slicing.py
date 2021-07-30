#         43210987654321
#         012345678901234
parrot = "Norwegian Blue"
game = "we have to win"
print(parrot[0:2])# 0 upto but not including 2
print(parrot[10:14])

print(parrot[:5])#norwe
print(parrot[0:5])#norwe

print(parrot[6:])#ian blue
print(parrot[6:14])#ian blue

print(parrot[:5] + parrot[5:])#Norwegian blue
print(parrot[:])#norwegian blue

#negative slicing
#1st number greater than second
print(parrot[-10:5])#e
print(game[-14:2])#we
print(game[-3:15])#win
print(parrot[3:-1])#wegian blu