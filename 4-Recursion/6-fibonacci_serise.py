def fib(n):
    #your code goes here
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))

class Solution:
    def fib(self, n):
        #your code goes here
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)