class Solution:
    def moveZeroes(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[k] = nums[k],nums[i]
                k += 1
        return nums
p1 = Solution()

print(p1.moveZeroes([1,2,0,4,5,0]))