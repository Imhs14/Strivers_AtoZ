class Solution:
    def sortarray(self,nums):

        def ms(nums,low, high):
            mid = (low + high)//2
            if low >= high: return
        
            ms(nums,low,mid)
            ms(nums,mid+1,high)
            merge(nums,low, mid,high)
        

        def merge(nums,low,mid,high):
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if nums[left] < nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
                    
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= high:
                temp.append(nums[right])
                right += 1

            for i in range(low,high+1):
                nums[i] = temp[i - low]
        ms(nums,0,len(nums)-1)

        return nums

p = Solution()

print(p.sortarray([5,2,3,1]))

print(p.sortarray([5,1,1,2,0,0]))