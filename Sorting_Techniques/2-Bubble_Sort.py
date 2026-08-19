class Solution:
    def bubblesort(self,nums):
        for i in range(len(nums),-1,-1):
            for j in range(i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums

p1 = Solution()
print(p1.bubblesort([13,46,24,52,20,9]))

# [9, 13, 20, 24, 46, 52]