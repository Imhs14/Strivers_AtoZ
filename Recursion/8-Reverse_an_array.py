class Solution:
    def reverse(self, arr: list, n: int,k=0) -> None:
        if k <= len(arr) // 2:
            arr[k],arr[len(arr)-k-1] = arr[len(arr)-k-1],arr[k]
        else:
            return arr
        return self.reverse(arr,n,k+1)

ip = Solution()
print(ip.reverse([1,2,3,4,5],5))