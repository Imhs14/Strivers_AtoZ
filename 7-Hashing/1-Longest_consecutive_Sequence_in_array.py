"""class Solution:
    def longestConsecutive(self, nums):
        c = 0
        n = len(nums)
        for i in range(n):
            if nums[i] < n:
                c += nums[i]
        res = (n*(n-1))/2
        return res == c

s = Solution()
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))"""
