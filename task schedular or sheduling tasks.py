'''
You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

Example 1:

Input: [a, a, a, b, c, c], K=2
Output: 7
Explanation: a -> c -> b -> a -> c -> idle -> a
Example 2:

Input: [a, b, a], K=3
Output: 5
Explanation: a -> b -> idle -> idle -> a
'''
from heapq import *


def task_schedular(tasks, k):

    interval_count = 0
    dict = {}

    for char in tasks:
        if char not in dict:
            dict[char] = 0

        dict[char] += 1

    max_heap = []

    for char, freq in dict.items():
        heappush(max_heap, (-freq, char))

    while max_heap:

        wait_list = []

        n = k + 1

        print(max_heap)

        while n > 0 and max_heap:

            interval_count += 1

            freq, char = heappop(max_heap)

            if -freq > 1:
                # decrement the freq and add to the wait_list
                wait_list.append((freq+1, char))

            n -= 1

        # put all the waiting list back on the heap
        for freq, char in wait_list:
            heappush(max_heap, (freq, char))

        if max_heap:
            # idle count
            print(n)
            interval_count += n

    return interval_count


print(task_schedular(['a', 'a', 'a', 'b', 'c', 'c'], 2))
