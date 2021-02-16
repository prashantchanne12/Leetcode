'''
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example 1:

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
occur in any of the two rooms later.
Example 2:

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
Example 3:

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to 
hold all the meetings.
 
Example 4:

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
 
'''
from heapq import *


def min_meeting_rooms(meetings):

    if meetings == None or len(meetings) == 0:
        return 0

    # sort the meetings by their start time
    meetings.sort()

    min_rooms = 0
    min_heap = []

    for meeting in meetings:

        # remove all the meetings that have ended
        while len(min_heap) > 0 and meeting[0] >= min_heap[0][1]:
            heappop(min_heap)

        # add the current meeting into min_heap
        heappush(min_heap, meeting)

        print(min_heap)

        # all active meetings are in the min_heap, sow need rooms for all of them
        min_rooms = max(min_rooms, len(min_heap))

    return min_rooms


print(min_meeting_rooms([[4, 5], [2, 3], [2, 4], [3, 5]]))
