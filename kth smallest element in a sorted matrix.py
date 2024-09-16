'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    
        rows = len(matrix[0])
        cols = len(matrix)
        
        left = matrix[0][0]
        right = matrix[cols-1][rows-1]
        k-=1

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


                        

                
