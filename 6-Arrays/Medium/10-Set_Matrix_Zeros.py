class Solution:
    def setZeroes(self, matrix):
        # Your code goes here
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    k = 0
                    while k < len(matrix):
                        matrix[k][j] = 0
                        k += 1
                    matrix[i] = [0]*len(matrix[0])
                    
        return matrix

p = Solution()

print(p.setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]
print(p.setZeroes( [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))    # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(p.setZeroes([[1,2,3,4],[5,6,0,8],[9,10,11,12]]))  #[[1,2,0,4],[0,0,0,0],[9,10,0,]]

class Solution:
    def setZeroes(self, matrix):
        # Your code goes here
        js = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    pass