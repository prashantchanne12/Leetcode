'''
Given an array of meeting time intervals consisting of start and end times `[(s1,e1),(s2,e2),...] (si < ei)`, determine if a person could attend all meetings.

- 0≤intervals.length≤1040≤*intervals*.*length*≤104
- intervals[i].length==2*intervals*[*i*].*length*==2
- 0≤starti<endi≤1060≤*starti*<*endi*≤106
- `[(0,8), (8,10)]` is not conflict at **8**

**Example**

**Example1**

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30), (5,10) and (0,30),(15,20) will conflict

```

**Example2**

```
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation:
Two times will not conflict

```
'''

def meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    
    prev_start, prev_end = intervals[0]
    
    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        
        if current_start < prev_end:
            return False
            
        prev_start = current_start
        prev_end = current_end
    
    return True
    
    
intervals = [[6,7], [2,4], [8,12]]
intervals = [[1,4], [2,5], [7,9]]
print(meeting_rooms(intervals))