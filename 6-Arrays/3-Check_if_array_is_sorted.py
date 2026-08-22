class Solution:
    def isSorted(self, nums):
        #your code goes here
        for i in range(1,len(nums)):
            if nums[i]< nums[i-1]:
                return False
        return True

p1 = Solution()
print(p1.isSorted([1, 2, 1, 4, 5]))
print(p1.isSorted([1, 2, 3, 4, 5]))