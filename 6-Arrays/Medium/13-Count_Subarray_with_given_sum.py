class Solution:
    def subarraySum(self, nums, k):
        count = 0
        # Brute Force solution
        
        for i in range(len(nums) - 1):
            s = 0
            for j in range(i + 1,len(nums)):
                s += nums[j]
                if s == k:
                    count += 1
        return count
p = Solution()
print(p.subarraySum([1,1,1],2))
print(p.subarraySum([1,2,3],3))
print(p.subarraySum([3,1,2,4],6))