def pattern9(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(2*i-1):
            print("*",end="")
        print()
    for i in range(1,n+1):
        print(" "*(i-1),end="")
        for j in range(2*(n-i)+1):
            print("*",end="")
        print()

pattern9(4)

"""
n = 5

    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""