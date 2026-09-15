class Solution:
    def pascalTriangleI(self, r, c):
        if r == 1: return [[1]]
        res = [[1]]
        re1 = []
        i,j = 1,0
        while i < r:
            if j == 0:
                re1.append(1)
                j += 1
            elif j < i:
                while j < i:
                    sum_val = res[i-1][j] + res[i-1][j-1]
                    re1.append(sum_val)
                    j += 1

            if j == i:
                re1.append(1)
                res.append(re1)
                re1 = []
                j = 0
                i += 1

        result = res[r-1][c-1]
        return result

p = Solution()
print(p.pascalTriangleI(4,2))
print(p.pascalTriangleI(5,3)) 

# Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.