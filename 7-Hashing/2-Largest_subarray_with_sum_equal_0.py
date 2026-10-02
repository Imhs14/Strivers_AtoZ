class Solution:
    def maxLen(self, nums):
        # Your code goes here
        seen = {0:-1}
        csum = 0
        best = 0
        for i,x in enumerate(nums):
            csum += x
            if csum in seen:
                best = max(best,i - seen[csum])
            else:
                seen[csum] = i
        return best

s = Solution()
print(s.maxLen([15, -2, 2, -8, 1, 7, 10, 23]))
print(s.maxLen([1, 0, -4, 3, 1, 0]))
print(s.maxLen( [2, 10, 4]))