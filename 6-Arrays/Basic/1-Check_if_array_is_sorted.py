class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

p = Solution()
print(p.arraySortedOrNot([5,4,6,7,8],5))
print(p.arraySortedOrNot([1,2,3,4,5],5))