class Solution:
    def Insertionsort(self,nums):
        n = len(nums)
        for i in range(n):
            for j in range(i,0,-1):
                if nums[j] < nums[j-1]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
                print(nums,'after',' and i=',i,'j=',j)
        return nums
                    

p1 = Solution()
print(p1.Insertionsort([14,9,15,12,6,8,13]))

#for i in range(5,-1,-1):
#    print(i)