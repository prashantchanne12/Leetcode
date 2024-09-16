'''
**Problem Statement:**Given a row-wise sorted matrix of size MXN, where M is no. of rows and N is no. of columns, find the median in the given matrix.
Note:MXN is odd.

Example 1:
Input Format:M = 3, N = 3, matrix[][] =

                    1 4 9 
                    2 5 6
                    3 8 7
                    
Result: 5
Explanation:  If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. So, median = 5
Example 2:
Input Format:M = 3, N = 3, matrix[][] =

                    1 3 8 
                    2 3 4
                    1 2 5
                    
Result: 3
Explanation:  If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8. So, median = 3
'''

def find_median(matrix):
    
    left = 1
    right = 2000
    k = (len(matrix) * len(matrix[0])) // 2
    
    def find_elements_less_than_mid(target):
        total = 0
        
        for i in range(len(matrix)):
            arr = matrix[i]
            
            left = 0
            right = len(matrix[0])-1
            count = 0
            
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            total += left
        
        return total
    
    while left <= right:
        mid = (left + right) // 2
        
        elements_less_than_mid = find_elements_less_than_mid(mid)
        
        if elements_less_than_mid <= k:
            left = mid + 1
        else:
            right = mid - 1
            
    
    return left
    
matrix = [
    [10, 11, 12],
    [15, 16, 17],
    [1, 2, 3]
]
print(find_median(matrix))
        