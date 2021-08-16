'''
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
'''


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]

        for i in range(max(len(v1), len(v2))):

            if i > len(v1)-1:
                version1 = 0
            else:
                version1 = v1[i]

            if i > len(v2)-1:
                version2 = 0
            else:
                version2 = v2[i]

            if version1 > version2:
                return 1
            elif version2 > version1:
                return -1

        return 0
