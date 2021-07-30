name = "j2e3el4a5n6i"
s=""
si=""


for char in name:
    if not char.isnumeric():
        s = s + char
    else:
        si=si +char

print(s)
print(si)

# a = [[3 , 4 , 5],
#     [2 , 3 , 4]]
#
# b= [[ 1 , 2 , 3],
#     [3 , 5 , 7 ]]
#
# c= [[0, 0, 0],
#     [0, 0, 0]]
#
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         c[i][j]=a[i][j] + b[i][j]
#
# for r in c:
#     print(r)
