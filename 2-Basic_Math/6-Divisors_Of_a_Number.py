class Solution:
    def divisors(self, n):
        divisorr = []
        for i in range(1,n + 1):
            if n % i == 0:
                divisorr.append(i)
        return divisorr

"""
Input: n = 6
Output = [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, 6.
"""