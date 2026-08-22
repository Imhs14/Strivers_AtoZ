class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n
        for i in range(k,n):
            nums[i-k],nums[i] = nums[i],nums[i-k]

        return nums

p1 = Solution()

print(p1.rotateArray([1,2,3,4,5,6],2))

print(p1.rotateArray([3, 4, 1, 5, 3, -5],8))
# Try right rotating 