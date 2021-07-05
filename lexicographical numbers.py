'''
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
'''


def numbers_lexi(n):
    arr = [str(i) for i in range(1, n+1)]
    arr.sort()
    arr = [int(num) for num in arr]
    return arr


def numbers_lexi_2(n):
    arr = [i for i in range(1, n+1)]
    arr.sort(key=str)
    return arr


def numbers_lexi_3(n):
    arr = [i for i in range(1, n+1)]
    arr.sort(key=str)
    return arr
