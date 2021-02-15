'''
Given a list of appointments, find all the conflicting appointments.

Example:

Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output: 
[4,5] and [3,6] conflict. 
[3,6] and [5,7] conflict.
 
'''


def can_attend_all_appointments(intervals):

    # sort the intervals
    intervals.sort()

    str = ''

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):

        interval = intervals[i]

        if end > interval[0]:
            str += '{0} and {1} conflict \n'.format(
                [start, end], [interval[0], interval[1]])
        else:
            # update start and end
            start = interval[0]
            end = interval[1]

    return str


print(can_attend_all_appointments([[4, 5], [2, 3], [3, 6], [5, 7], [7, 8]]))
