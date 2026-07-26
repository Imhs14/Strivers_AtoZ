class Solution:
    def pattern7(self, n):
        for i in range(1,n+1):
            print(" "*(n-i),end="")
            for j in range(2*i-1):
                print("*",end="")
            print()
"""
n = 4
    *
   ***
  *****
 *******
*********
"""