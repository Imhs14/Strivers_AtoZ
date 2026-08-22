class Solution:
    def rotateArrayByOne(self, nums):
        for i in range(1,len(nums)):
            nums[i],nums[i-1] = nums[i-1],nums[i]
        return nums

p1 = Solution()

print(p1.rotateArrayByOne( [1, 2, 3, 4, 5]))

print(p1.rotateArrayByOne( [-1, 0, 3, 6]))  