class Solution:
    def rotateMatrix(self, matrix):
        # First taking the Transpose
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        n = len(matrix[0]) - 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                matrix[i][j],matrix[i][n - j] = matrix[i][n - j],matrix[i][j]
        return matrix

p = Solution()
print(p.rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))    #  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(p.rotateMatrix([[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]))     #  [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]
print(p.rotateMatrix([[1, 1, 2], [5, 3, 1], [5, 3, 5]]))