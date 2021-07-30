available=["jar" , "tea" , "pot"]
rchoices = []
for i in range(1 , len(available) + 1):
    rchoices.append(str(i))
print(rchoices)
choice="-"
parts_need = []

while choice != '0':
    if choice in rchoices:
        print("adding {0}".format(choice))
        index = int(choice) - 1
        chose = available[index]
        parts_need.append(chose)
    else:
        print("try these")
        for num,part in enumerate(available):
            print("{0}: {1}".format(num + 1 , part))

    choice = input()

print("your list is as below:")
print(parts_need)