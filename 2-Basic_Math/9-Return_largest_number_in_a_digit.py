class Solution:
    def largestDigit(self, n):
        maxx = 0
        for i in range(len(str(n))):
            digit = n % 10
            if digit > maxx:
                maxx = digit
            n //= 10
        return maxx

p = Solution()
print(p.largestDigit(99))
print(p.largestDigit(25))