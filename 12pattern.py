n =int(input())
# n > 2
for i in range(1,n+1):
    for j in range(1,(n*2)+1):
        if j <= i:
            print(j,end="")
        elif (n*2) - j < i:
            print(i,end="")
            i -= 1
        else:
            print(" ",end="")
    print()


"""
n = 5
1        1
12      21
123    321
1234  4321
1234554321
"""