class Solution:
    def insertionSort(self, nums):

        def ris(nums,n=0):
            if n == len(nums):
                return nums     # When we hit the base case of n being equal to the len array
            
            for i in range(n,0,-1):
                if nums[i] < nums[i-1]:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
                else:
                    break

            return ris(nums,n+1)    # This is will do that outer loop's work of incrementing our n 
        return ris(nums)            # This runs only 1 time to delivery the nums array to inner function

p = Solution()
print(p.insertionSort([13,46,52,20,9]))



def RIS(nums,n=0):
    if n == len(nums):
        return
    for i in range(n,0,-1):
        if nums[i] < nums[i-1]:
            nums[i],nums[i-1] = nums[i-1],nums[i]
        else:
            break
    return RIS(nums,n+1) or nums

print(RIS([13,46,52,20,9]))
print(RIS([9,8,4,2,6,1,4,9]))