"""from collections import defaultdict
def cfreq(n):
    hs = defaultdict(int)
    for x in n:
        hs[x] += 1
    z = []
    for i,j in hs.items():
        z.append([i,j])
        
    print(z)
cfreq([2,1,1,3,4,2])"""
from collections import defaultdict
class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        hsh = defaultdict(int)
        for x in nums:
            hsh[x] += 1
        z = []
        for i,j in hsh.items():
            z.append([i,j])
        return z
p1 = Solution()
print(p1.countFrequencies([1, 2, 2, 1, 3]))