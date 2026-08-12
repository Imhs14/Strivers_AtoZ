class Solution:
    def reverseNumber(self, n):
        result = 0
        while n > 0:
            digit = n % 10
            result = result * 10 + digit
            n //= 10
        return result

"""
Input: n = 25
Output: 52
Explanation: Reverse of 25 is 52.
"""