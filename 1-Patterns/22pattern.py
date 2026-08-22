"""
n = 5

5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
"""
def pattern22(n):
    # The size of our grid is 2n - 1
    size = 2 * n - 1
    
    for i in range(size):
        for j in range(size):
            # 1. Calculate distance from all 4 edges
            top = i
            left = j
            bottom = (size - 1) - i
            right = (size - 1) - j
            
            # 2. Find the minimum distance to any edge
            min_dist = min(top, left, bottom, right)
            
            # 3. Print n minus that minimum distance
            print(n - min_dist, end=" ")
        
        # Move to the next line after finishing a row
        print()

pattern22(4)