'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
'''

# Solution 1
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dict = {} # for counting incoming edges
        visited = set() # If A -> B, then A can't be the Judge. Adding A to the visited

        if n == 1 and len(trust) == 0:
            return 1

        for person1, person2 in trust:
            if person2 not in dict:
                dict[person2] = []

            dict[person2].append(person1)
            visited.add(person1)

        for key, val in dict.items():
            if len(val) == n - 1 and key not in visited:
                return key

        return -1

# Soluiton 2
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for person1, person2 in trust:
            incoming[person2] += 1
            outgoing[person1] += 1

        for i in range(1, n+1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i

        return -1

# Solution 3
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for person1, person2 in trust:
            incoming[person2] += 1
            outgoing[person1] += 1

        for i in range(1, n+1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i

        return -1