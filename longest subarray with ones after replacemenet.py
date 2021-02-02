'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''


def ones_after_replacement(nums, k):

    window_start = 0
    max_length = 0
    max_ones = 0

    for window_end in range(0, len(nums)):

        if nums[window_end] == 1:
            max_ones += 1

        if (window_end-window_start+1) - max_ones > k:
            # shrink the window from start
            if nums[window_start] == 1:
                max_ones -= 1

            window_start += 1

        max_length = max(max_length, (window_end-window_start+1))

    return max_length


print(ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
