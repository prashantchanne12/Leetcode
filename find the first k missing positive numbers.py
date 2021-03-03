'''
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
'''


def find_first_k_missing_positive(nums, k):

    n = len(nums)
    i = 0

    while i < n:
        j = nums[i] - 1

        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    extra_numbers = set()

    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i+1)
                extra_numbers.add(nums[i])

    # add the remaining numbers
    i = 1
    while len(missing_numbers) < k:
        candidate_number = i + n

        # ignore if the extra_array contains the candidate number
        if candidate_number not in extra_numbers:
            missing_numbers.append(candidate_number)

        i += 1

    print(missing_numbers)


find_first_k_missing_positive([2, 3, 4], 3)
