class Solution:
    def subarraySum(self, nums, k):
        # Brute Force solution
        count = 0
        n = len(nums)
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                if s == k:
                    count += 1
        return count
p = Solution()
print(p.subarraySum([1,1,1],2))
print(p.subarraySum([1,2,3],3))
print(p.subarraySum([3,1,2,4],6))

# Optimal Solution 
# Time = O(N), Space = O(N)
class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        count = 0
        prefix_sum = [0]* n
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        m = {}
        for j in range(n):
            prefix_i_1 = prefix_sum[j] - k

            if prefix_sum[j] == k:
                count += 1

            if prefix_i_1 in m:
                count += m[prefix_i_1]

            if prefix_sum[j] not in m:
                m[prefix_sum[j]] = 0
            m[prefix_sum[j]] += 1

        return count

p = Solution()

print(p.subarraySum([1,1,1],2))

print(p.subarraySum([1,2,3],3))
print(p.subarraySum([9,4,0,20,3,10,5],33))