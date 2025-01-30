'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        window_start = 0
        window_end = 0

        while window_end < len(nums):
            # pop smaller values from the q
            while q and nums[q[-1]] < nums[window_end]:
                q.pop()

            q.append(window_end)

            # if the left value is out of bounds
            if window_start > q[0]:
                q.popleft()

            if window_end + 1 >= k:
                res.append(nums[q[0]])
                window_start += 1
            
            window_end += 1

        return res




