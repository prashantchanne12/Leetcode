'''
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
'''

def sort_array(intervals):
    arr = []
    
    intervals.sort()
    
    for nums in intervals:
        nums.sort()
        
        arr.append(nums)
    
    
    return arr

def insert(intervals, new_intervals):
    
    intervals.append(new_intervals)
    
    # sort the array
    arr = sort_array(intervals)
    
    start = arr[0][0]    
    end = arr[0][1]    
    merged = []
    
    for i in range(1, len(intervals)):
        
        interval = intervals[i]
        
        if interval[0] <= end:
            # merge the overlap array
            end = max(end, interval[1])
            
        else:
            merged.append([start, end])
            # update the start end
            start = interval[0]
            end = interval[1]

    # add the last interval
    merged.append([start, end])
    
        
    return merged
    
    
print(insert([[1,3], [5,7], [8,12]], [4,6]))