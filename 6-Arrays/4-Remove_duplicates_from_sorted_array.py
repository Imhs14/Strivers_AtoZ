class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

p1 = Solution()

print(p1.removeDuplicates([0, 0, 3, 3, 5, 6]))

print(p1.removeDuplicates([-2, 2, 4, 4, 4, 4, 5, 5]))