class Solution:
    def GCD(self, n1, n2):
        gcd = 0
        m = max(n1,n2)
        for i in range(1,m+1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
        return gcd
"""
Input: n1 = 4, n2 = 6
Output: 2
Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
Greatest Common divisor = 2.
"""