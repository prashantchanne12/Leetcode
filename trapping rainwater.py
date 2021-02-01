'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''

class Solution(object):
    def trap(self, height):
        
        total_water = 0
        max_left = 0
        max_right = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            
            if height[left] <= height[right]:
                
                if height[left] >= max_left:
                    # cant form a wall, current pointer has greater height
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                    
                left += 1
                
            else:
                
                if height[right] >= max_right:
                    # cant form a wall, current pointer has greater height
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                    
                right -= 1
                
        return total_water