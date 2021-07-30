grocery = ["bread" , "butter" , "eggs" , "maggi"]

for check in grocery:
    if check == "bread" or check == "eggs":
        continue #it terminates the below code if condition is satisfied but only for given condition

    print(check)
print(".....")
for iss in grocery:
    if iss == "eggs":
        break # it completely terminates the code below it

    print(iss)


