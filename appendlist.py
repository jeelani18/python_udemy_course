pre_house_hold = ["mat", "mob", "camphor", "hdmi cable"]
valid_choices = []
for i in range(0, len(pre_house_hold) ):
    valid_choices.append(str(i))
print(valid_choices)
choice = "-"
house_hold = []

while choice != '0':
    if choice in valid_choices:
        print("adding {}".format(choice))
        index = int(choice)
        chosen_one = pre_house_hold[index]
        house_hold.append(chosen_one)
    else:
        print("try adding below options:")
        for i in range(len(pre_house_hold)):
            for j in range(len(pre_house_hold)):
                print("{0}: {1}".format(i,j))

        #for serial, items in enumerate(pre_house_hold):
         #   print("{0}: {1}".format(serial, items))

    choice = input()

print(house_hold)

# if choice == '1':
#     house_hold.append("mat")
# elif choice == '2':
#     house_hold.append("mob")
# elif choice == '3':
#     house_hold.append("camphor")
# elif choice == '4':
#     house_hold.append("hdmi cabl")