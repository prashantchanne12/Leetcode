'''
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].

Example 2:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 3:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


def sort_array(intervals):
    arr = []
    
    # sort outer elements
    intervals.sort()
    
    # sort inner elements
    for nums in intervals:
        nums.sort()
        arr.append(nums)
    
    return arr

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals) <= 1:
            return intervals
        
        # sort 2D array of intervals
        arr = sort_array(intervals)
        
        merged_array = []
        
        start = arr[0][0]
        end = arr[0][1]
        
        for i in range(1,len(intervals)):
            
            interval = intervals[i]
            
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                merged_array.append([start, end])
                # update the start and end
                start = interval[0]
                end = interval[1]
                
        # add the last interval
        merged_array.append([start, end])
        
        return merged_array