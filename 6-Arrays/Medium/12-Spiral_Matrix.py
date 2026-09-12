class Solution:
    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result

        i,j = 0,0
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        total_elements = len(matrix) * len(matrix[0])

        while len(result) < total_elements:

            # Moving top left to top right 
            for j in range(left,right + 1):
                result.append(matrix[top][j])
            top += 1

            # Moving from top right to bottom right
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Moving bottom left to bottom right
            if top <= bottom:
                for j in range(right,left - 1,-1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom,top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            
        return result
p = Solution()

print(p.spiralOrder([[1, 2, 3], [4 ,5 ,6], [7, 8, 9]])) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(p.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8]])) # [1, 2, 3, 4, 8, 7, 6, 5]
print(p.spiralOrder([[1, 2], [3, 4], [5, 6], [7, 8]])) # [1, 2, 4, 6, 8, 7, 5, 3]