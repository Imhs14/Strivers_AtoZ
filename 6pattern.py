class Solution:
    def pattern6(self, n):
        for i in range(1,n+1):
            for j in range(j,n - i - 2):
                print(j,end=" ")
            print()

"""
n = 4
O/P:
12345
1234
123
12
1
"""