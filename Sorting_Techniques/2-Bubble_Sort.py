class Solution:
    def bubblesort(self,nums):
        didswap = 0 # Optimization, after 1st iteration if the didswap remains to be 0 we quickly return the array, hence making it a O(n) Time complexity.
        for i in range(len(nums),-1,-1):
            for j in range(i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    didswap += 1
            if didswap == 0:
                return nums
        return nums

p1 = Solution()
print(p1.bubblesort([13,46,24,52,20,9]))    # Time complexity gets to O(n^2)

print(p1.bubblesort([1,2,3,4,5]))  # Best case Time complexity falls to O(n)
# [9, 13, 20, 24, 46, 52]

# SPace in the both the cases will be O(1),bcs no allocations of extra spaces 