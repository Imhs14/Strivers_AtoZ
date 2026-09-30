class Solution:
    def primeUptoN(self, n):
        result = []
        def prime(m):
            if m < 2: return False
            for i in range(2,int(m**0.5)+1):
                if m % i == 0:
                    return False
            return True

        for i in range(n+1):
            if prime(i):
                result.append(i)
        return len(result)

p = Solution()
print(p.primeUptoN(6))