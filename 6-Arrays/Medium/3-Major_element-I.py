class Solution:
    def majorityElement(self, nums):
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            
            if ans == num:
                count += 1
            else:
                count -= 1
        return ans

p = Solution()
print(p.majorityElement([7,0,0,1,7,7,2,7,7]))