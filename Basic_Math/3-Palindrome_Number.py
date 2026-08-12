class Solution:
    def isPalindrome(self, n):
        m = n
        result = 0
        while m > 0:
            digit = m % 10
            result = result * 10 + digit
            m //= 10
        return result == n

"""
Input: n = 123
Output: false
Explanation: When read from left to right : 123.
When read from right to left : 321.
"""