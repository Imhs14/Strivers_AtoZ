class Solution:
    def singleNumber(self, nums):
        #your code goes here
        hsh = {}
        for i in range(len(nums)):
            if nums[i] not in hsh.keys():
                hsh[nums[i]] = 1
            else:
                hsh[nums[i]] += 1

        result = min(hsh,key = lambda x: hsh[x])
        return result

p = Solution()

print(p.singleNumber([1, 2, 2, 4, 3, 1, 4]))