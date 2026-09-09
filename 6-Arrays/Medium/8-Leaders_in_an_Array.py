class Solution:
    def leaders(self, nums):
        n = len(nums) - 1
        GN = nums[-1]
        ans = [GN]
        for i in range(n-1,-1,-1):
            if nums[i] > GN:
                ans.insert(0,nums[i])
                GN = nums[i]

        return ans

p = Solution()
print(p.leaders([1, 2, 5, 3, 1, 2]))
print(p.leaders([-3, 4, 5, 1, -4, -5]))
print(p.leaders( [-3, 4, 5, 1, -30, -10]))