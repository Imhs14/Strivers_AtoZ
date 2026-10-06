class Solution:
    def pascalTriangleII(self, r):
        if r == 1: return [1]
        res = [[1]]
        res1 = []
        i,j = 1,0
        while i <= r:
            if j == 0:
                res1.append(1)
                j += 1
            elif j < i:
                a = res[i-1][j] + res[i-1][j-1]
                res1.append(a)
                j+=1
            elif j == i:
                res1.append(1)
                res.append(res1)
                res1 = []
                j = 0
                i += 1
        return res[r-1]

s = Solution()
print(s.pascalTriangleII(4))
print(s.pascalTriangleII(5))