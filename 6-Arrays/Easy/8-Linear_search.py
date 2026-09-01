class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

p = Solution()

print(p.linearSearch([2, 3, 4, 5, 3],3))