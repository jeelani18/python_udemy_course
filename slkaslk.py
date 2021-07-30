from array import *
n=int(input("enter number of scores: "))
c = array('i', [int(input())])

for i in range(len(c)+1):
    if max(c)-1==i:
        print(i)


