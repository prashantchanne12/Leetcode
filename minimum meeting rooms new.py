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

import heapq


def min_meeting_rooms(meetings):

    if not meetings:
        return 0

    # sort the meetings by their start time
    meetings.sort(key=lambda x: x[0])

    # rooms used min heap
    rooms_used = []

    # push the first meeting to heap
    heapq.heappush(rooms_used, meetings[0][1])

    for i in range(1, len(meetings)):

        meeting = meetings[i]

        # check if the end time of current meeting is greater than or equal to meeting in the heap
        # if true this means they don't overlap and we can use the same meeting room
        if meeting[0] >= rooms_used[0]:
            heapq.heappop(rooms_used)

        # push current meeting's end time into the heap
        # so later on we would know when this meeting is going to end
        heapq.heappush(rooms_used, meeting[1])

    return len(rooms_used)


print(min_meeting_rooms(([[4, 5], [2, 3], [2, 4], [3, 5]])))
