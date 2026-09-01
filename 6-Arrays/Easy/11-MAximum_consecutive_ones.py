class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxx = 0
        prev = 0
        for num in nums:
            if num == 1:
                prev += 1
            elif num == 0:
                if prev > maxx:
                    maxx = prev
                prev = 0
        return max(maxx,prev)

p = Solution()

print(p.findMaxConsecutiveOnes([1,1,0,0,1,0,1,0,1,1,1]))