class Solution:
    def largestElement(self, nums):
        maxx = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > maxx:
                maxx = nums[i]
        return maxx

p1 = Solution()
print(p1.largestElement([3, 3, 0, 99, -40]))