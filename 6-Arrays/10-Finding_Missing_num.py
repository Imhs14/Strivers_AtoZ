class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected = n*(n + 1)//2 - sum(nums) # Gaussian sum 
        return expected

p1 = Solution()

print(p1.missingNumber( [0, 2, 3, 1, 4]))