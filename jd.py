available_parts = ["cd", "hard disk", "ram", "desktop"]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
choice = '-'
computer_parts = []

while choice != '0':
    if choice in valid_choices:
        print("adding {}".format(choice))
        index = int(choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("only chose from below options:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    choice = input()

print(computer_parts)

