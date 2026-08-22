def ss(n):
    for i in range(len(n) - 1):
        minn,ind = n[i],i
        for j in range(i+1,len(n)):
            if n[j] < minn:
                minn,ind = n[j],j
        n[ind],n[i] = n[i],n[ind]
    return n

print(ss([5 ,4 ,4 ,1 ,1]))

class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)-1):
            minn,ind = nums[i],i
            for j in range(i + 1,len(nums)):
                if nums[j] < minn:
                    minn,ind = nums[j],j
            nums[ind],nums[i] = nums[i],nums[ind]
        return nums
p1 = Solution()
print(p1.selectionSort([7 ,4 ,1 ,5 ,3]))

# Time = O(n^2) approx, Space = O(1)

# [1, 1, 4, 4, 5] 

# [1, 3, 4, 5, 7]
