op = "-"

while True:
    if op == "0":
        break
    elif op in "1234":
        print("you chose to {}".format(op))
    else:
        print("you chose {}".format(op))
        op=input("choose your option again:\n"
              "1.learn python\n"
              "2.learn java\n"
              "3.go swimming\n"
              "4.go to bed\n"
              "0.exit")

    op = input()