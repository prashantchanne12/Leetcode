class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print('[' + str(self.start) + ',' + str(self.end) + ']', end='')


def find_employee_free_time(schedule):

    # error checking
    if schedule is None:
        return []

    # break down the intervals
    intervals = []
    for emp in schedule:
        for interval in emp:
            intervals.append([interval.start, interval.end])

    # sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # loop through the intervals to find free time
    res = []
    last_end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]

        start = interval[0]
        end = interval[1]

        if start > last_end:
            # intervals do not overlap
            res.append([last_end, start])

        # update last_end
        last_end = max(last_end, end)

    return res


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print(find_employee_free_time(input))


main()
