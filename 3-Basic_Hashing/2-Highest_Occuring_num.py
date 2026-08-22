from collections import defaultdict
class Solution:
    def mostFrequentElement(self, nums):
        hsh = defaultdict(int)
        for x in nums:
            hsh[x] += 1
        
        return max(hsh, key= lambda k : hsh[k])

p1 = Solution()
print(p1.mostFrequentElement([1,2,2,2,3,3,3,2,2]))