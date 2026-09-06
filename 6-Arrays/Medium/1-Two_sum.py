class Solution:
    def twoSum(self, nums, target):
        seen = {nums[0]:0}
        
        for i in range(1,len(nums)):
            diff = target - nums[i]
            
            if diff in seen.keys() and ( i != seen[diff]):
                return [seen[diff],i]
            
            seen[nums[i]] = i
        
p = Solution()

print(p.twoSum([1, 6, 2, 10, 3],7))
print(p.twoSum([1, 3, 5, -7, 6, -3],0))