def Rbs(arr, n):
    if n == 1:      # very imp base case return when the n is equal to 1
        return 
    didswap = False
    for i in range(n-1):        # we are running this loop to swap, as we cannot do this swapping function in a recursive call
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
        didswap = True

    if not didswap:     # This will give us an optimal solution by checking is any swaps have been taken place, if not we will exit early (in case of the array being already sorted)
        return 
    Rbs(arr,n-1)     # As our array pushes the max to end we will have our array sorted from very end, so here we will keep decreasing the n the lenght of the arr with this recursive call
    return arr
arr = [1,9,7,4,2,3,5]
n = len(arr)
print(Rbs(arr,n))

# Time = O(n^2) for avg and worst, Best Case being O(n)
# Space = O(N) auxiliary stack space.

class Solution:
    def bubbleSort(self, nums):

        def Rbs(nums, n):
            if n == 1:
                return 
            didswap = False
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    didswap = True
            
            if not didswap:
                return 
            
            Rbs(nums,n-1)

        n = len(nums)
        Rbs(nums,n)
        return nums

p = Solution()

print(p.bubbleSort([1,9,7,4,2,3,5]))