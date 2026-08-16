def Nto1(n):
    if n == 0:
        return 0
    print(n)
    Nto1(n-1)
Nto1(5)

class Solution:
    def printNumbers(self, n):
        if n == 0:
            return
        print(n)
        self.printNumbers(n-1) # it is needed when you're dealing with the recursions