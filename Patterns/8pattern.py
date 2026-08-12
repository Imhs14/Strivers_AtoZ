def pattern8(n):
    for i in range(1,n+1):
        print(" "*(i-1),end="")
        for j in range(2*(n-i)+1):
            print("*",end="")
        print()

pattern8(4)

"""
n = 5
*********
 *******
  *****
   ***
    *
"""