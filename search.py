lists = ["hi" , "hello" , "gud aftr" , "gud evng"]

found = ""
find = input("enter word to find")

for index in range(4):
    if lists[index] == find:
        found = index
    print("found at ", found)

