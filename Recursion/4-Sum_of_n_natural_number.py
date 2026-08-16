def sumofn(n,total):
    if n == 0:
        print(total)
        return
    total += n
    sumofn(n-1,total)

sumofn(4,0)

class Solution:
    def NnumbersSum(self,N):
        #your code goes here
        def sumton(n, total):
            if n == 0:
                return total
            return sumton(n - 1, total + n)
        return sumton(N, 0)