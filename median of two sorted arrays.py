'''
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # we want B to be greater, A to be smaller
        if len(B) < len(A):
            B, A = A, B

        left = 0
        right = len(A) - 1

        while True:

            i = (left + right) // 2  # for A
            # for B (i starts at 0, j starts at 0 thats why extra -2)
            j = half - i - 2

            A_left = A[i] if i >= 0 else float('-infinity')
            A_right = A[i+1] if (i+1) < len(A) else float('infinity')

            B_left = B[j] if j >= 0 else float('-infinity')
            B_right = B[j+1] if (j+1) < len(B) else float('infinity')

            # partition is correct
            if A_left <= B_right and B_left <= A_right:
                # odd
                if total % 2:
                    return min(A_right, B_right)

                # even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1
