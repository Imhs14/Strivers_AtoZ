class Solution:
    def isArmstrong(self, n):
        m = n
        summ = 0
        while m > 0:
            digit = m % 10
            summ += digit ** 3
            m //= 10
        return summ == n
"""
Input: n = 153
Output: true
Explanation: Number of digits : 3.
13 + 53 + 33 = 1 + 125 + 27 = 153.
Therefore, it is an Armstrong number.
"""