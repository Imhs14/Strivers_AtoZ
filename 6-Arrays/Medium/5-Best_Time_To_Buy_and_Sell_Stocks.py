class Solution:
    def stockBuySell(self, arr,n):
        max_profit = 0  # This will compare the current profit to the maximum proit found earlier
        buy = arr[0]
       

        for i in range(1,len(arr)):
            profit = arr[i] - buy
            max_profit = max(profit, max_profit)

            if arr[i] < buy:
                buy = arr[i]


        return max_profit

p = Solution()

print(p.stockBuySell([10, 7, 5, 8, 11, 9],6)) # 6

print(p.stockBuySell([5, 4, 3, 2, 1],5)) # 0
print(p.stockBuySell([3, 8, 1, 4, 6, 2],6)) # 5   