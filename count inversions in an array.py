'''
Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).

What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].

Examples
Example 1:
Input Format
: N = 5, array[] = {1,2,3,4,5}
Result
: 0
Explanation
: we have a sorted array and the sorted array has 0 inversions as for i < j you will never find a pair such that A[j] < A[i]. More clear example: 2 has index 1 and 5 has index 4 now 1 < 5 but 2 < 5 so this is not an inversion.

Example 2:
Input Format
: N = 5, array[] = {5,4,3,2,1}
Result
: 10
Explanation
: we have a reverse sorted array and we will get the maximum inversions as for i < j we will always find a pair such that A[j] < A[i]. Example: 5 has index 0 and 3 has index 2 now (5,3) pair is inversion as 0 < 2 and 5 > 3 which will satisfy out conditions and for reverse sorted array we will get maximum inversions and that is (n)*(n-1) / 2.For above given array there is 4 + 3 + 2 + 1 = 10 inversions.

Example 3:
Input Format
: N = 5, array[] = {5,3,2,1,4}
Result
: 7
Explanation
: There are 7 pairs (5,1), (5,3), (5,2), (5,4),(3,2), (3,1), (2,1) and we have left 2 pairs (2,4) and (1,4) as both are not satisfy our condition. 

'''


from typing import List
import math

def merge(arr, left, mid, right) -> int:
    temp = []   
    i = left  
    j = mid + 1 

    pairs = 0     

    while (i <= mid and j <= right):
        if (arr[i] <= arr[j]):
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            pairs += (mid - left + 1) 
            j += 1

    while (i <= mid):
        temp.append(arr[i])
        i += 1

    while (j <= right):
        temp.append(arr[j])
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i - left]

    return pairs   

def mergeSort(arr : List[int], left : int, right : int) -> int:
    pairs = 0
    if left >= right:
        return pairs
    mid = (left + right) // 2
    pairs += mergeSort(arr, left, mid)    # left half
    pairs += mergeSort(arr, mid + 1, right)  # right half
    pairs += merge(arr, left, mid, right)  # merging sorted halves
    return pairs

def numberOfInversions(a : List[int], n : int) -> int:
    n = len(a)
    return mergeSort(a, 0, n - 1)

if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    n = 5
    pairs = numberOfInversions(a, n)
    print("The number of inversions are:", pairs)


