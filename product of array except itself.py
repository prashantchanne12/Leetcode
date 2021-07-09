'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''


def find_ans_1(nums):
    prev_mul = 1
    res = []

    for i in range(0, len(nums)):

        if i > 0:
            prev_mul *= nums[i-1]

        ans = 1

        for j in range(i+1, len(nums)):

            ans *= nums[j]

        print(ans, prev_mul)
        if i >= 1:
            ans *= prev_mul

        res.append(ans)

    return res


print(find_ans_1([1, 2, 3, 4]))


def find_ans_2(nums):

    res = 1

    for num in nums:
        res *= num

    ans = []

    for num in nums:
        ans.append(res//num)

    return ans


print(find_ans_2([1, 2, 3, 4]))


def find_ans_3(nums):
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix*nums[i]

    posfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = posfix*res[i]
        posfix = posfix*nums[i]

    return res


print(find_ans_3([1, 2, 3, 4]))
