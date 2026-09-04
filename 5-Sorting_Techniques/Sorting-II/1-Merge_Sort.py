class Solution:
    def sortarray(self,nums):

        def ms(nums,low, high):
            mid = (low + high)//2
            if low >= high: return  # base case we will stop the execution when our low is greater then our high.
        
            ms(nums,low,mid)        # This recursive call is for left part of the array
            ms(nums,mid+1,high)     # This recursive call if for the right part of the array
            merge(nums,low, mid,high)       # This the main recursive call that will sort the array and this is the only function we need to write the logic of merging,we don't write any specific code for dividing, it's being taken care in recursive calls and then in merging function i.e merge
        

        def merge(nums,low,mid,high):
            temp = []
            left = low                              # left goes from low to mid (Eg: 0-5)
            right = mid + 1                         # right goes from (mid + 1 to high) Eg: 6-10
            while left <= mid and right <= high:    # to prove above comments here we are moving from left i.e low i.e 0 and right is moving from mid + 1 to high that is till end of the 2nd array
                if nums[left] < nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
                    
            while left <= mid:              # loop runs when our left is still not fully merged
                temp.append(nums[left])
                left += 1
            while right <= high:            # This loop will runs when elements are still left out in our right array
                temp.append(nums[right])    
                right += 1

            for i in range(low,high+1):     # we are modifying the elements of the array nums with our temp array
                nums[i] = temp[i - low]
        ms(nums,0,len(nums)-1)  

        return nums

p = Solution()

print(p.sortarray([5,2,3,1]))

print(p.sortarray([5,1,1,2,0,0]))

"""
Merge sort has a time complexity of O(n log n) in all three cases — best, average, and worst case.

Why it's consistent across cases:

Merge sort always splits the array into halves and merges them back, regardless of the input's initial order. This gives:

Divide step: The array is split in half recursively, creating a recursion tree of depth log n (since you keep halving n until you reach size 1).
Merge step: At each level of the tree, merging all the sub-arrays back together takes O(n) work total (you touch every element once per level).

So total work = (work per level) × (number of levels) = O(n) × O(log n) = O(n log n).

Case	Time Complexity
Best	O(n log n)
Average	O(n log n)
Worst	O(n log n)

Space complexity: O(n) — it's not in-place, since merging requires auxiliary arrays to hold elements during the merge step.

Compare to quicksort: Quicksort is O(n log n) on average but degrades to O(n²) in the worst case (e.g., already-sorted input with a bad pivot choice).
 Merge sort's guaranteed O(n log n) makes it more predictable, which is why it's often preferred when worst-case performance matters — though quicksort tends to win in practice due to better cache locality and lower constant factors."""