class Solution:
    def secondLargestElement(self, nums):
        maxx = float('-inf')
        s_m = float('-inf')
        for i in range(len(nums)):
            if nums[i] > maxx:
                maxx = nums[i]

        for j in range(len(nums)):
            if nums[j] > s_m and nums[j] != maxx:
                s_m = nums[j]

        if s_m == float('-inf'):
            return -1

        return s_m 

p1 = Solution()
print(p1.secondLargestElement([2,3,4,8,5,9]))

print(p1.secondLargestElement([9,9,9,9,9,9]))