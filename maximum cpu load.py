'''
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
jobs are running at the same time i.e., during the time interval (2,4).
Example 2:

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.
Example 3:

Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].
'''

from heapq import *

def find_max_cpu_load(jobs):
    # sort the jobs by their start time
    jobs.sort(key = lambda x: x[0])
    
    start = 0
    end = 1
    cpu_load = 2
    
    max_cpu_load = 0
    current_cpu_load = 0
    min_heap = []
    
    for job in jobs:
        
        # remove all the jobs that have ended
        while len(min_heap) >  0 and min_heap[0][end] <= job[start]:
            current_cpu_load -= min_heap[0][cpu_load]
            heappop(min_heap)
        
        # add the current job into the min_heap 
        heappush(min_heap, job)
        
        current_cpu_load += job[cpu_load]
        max_cpu_load = max(max_cpu_load, current_cpu_load)
        
    return max_cpu_load
    

print(find_max_cpu_load([[1,4,3], [2,5,4], [7,9,6]]))      
print(find_max_cpu_load([[6,7,10], [2,4,11], [8,12,15]]))    
print(find_max_cpu_load([[1,4,2], [2,4,1], [3,6,5]]))    
