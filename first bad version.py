# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


def isBadVersion(version):
    return None


class Solution(object):
    def firstBadVersion(self, n):

        left = 1
        right = n
        res = 0

        while left <= right:

            mid = (left + right) // 2

            if isBadVersion(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
