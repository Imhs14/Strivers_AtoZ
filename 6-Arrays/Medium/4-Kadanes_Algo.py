class Solution:
    def maxSubArray(self, nums):
        curs = maxs = nums[0]
    
        for i in range(1,len(nums)):
            curs = max(nums[i],curs+nums[i])
            maxs = max(curs,maxs)
        
        return maxs

p = Solution()

print(p.maxSubArray([2, 3, 5, -2, 7, -4]))
print(p.maxSubArray([-2, -3, -7, -2, -10, -4]))