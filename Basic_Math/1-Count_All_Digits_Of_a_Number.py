class Solution:
    def countDigit(self, n):
        count = 0
        if n == 0: return 1
        while n > 0:
            count += 1
            n //= 10
        return count

"""
n = 123
o/p = 3
0 <= n <= 5000
"""