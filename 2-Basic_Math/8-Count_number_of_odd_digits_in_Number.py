class Solution:
    def countOddDigit(self, n):
        m = n
        count = 0
        for i in range(len(str(n))):
            digit = m % 10
            if digit % 2 != 0:
                count += 1
            m //= 10
        return count

p = Solution()
print(p.countOddDigit(123456789))
print(p.countOddDigit(15))