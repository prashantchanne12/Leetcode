'''
Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.

Example 1:

Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct   
[1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers 
in the 'originalSeq'. 

Example 2:

Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
Output: false
Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct 
[1, 2, 3, 4]. There are two possible sequences we can construct from the given sequences:
1) [1, 2, 3, 4]
2) [1, 2, 4, 3]

Example 3:

Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
Output: true
Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct 
[3, 1, 4, 2, 5].
'''

from collections import deque


def reconstruct_sequence(oringinal_seq, sequences):

    sorted_order = []

    if len(oringinal_seq) <= 0:
        return False

    # 1) Initiliaze the graph

    # count of incoming edges
    in_degrees = {}

    # count of adjecency list graph
    graph = {}

    for sequence in sequences:
        for num in sequence:
            in_degrees[num] = 0
            graph[num] = []

    # 2) Built the graph
    for parnet, child in sequences:
        graph[parnet].append(child)
        in_degrees[child] += 1

    # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
    if len(in_degrees) != len(oringinal_seq):
        return False

    # 3) Find all sources i.e. all nodes with 0 in-degrees
    sources = deque()

    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)

    # 4) For each source, add it to the sorted order and subtract on from all of its children
    # if child's in-degrees becomes zero, add it to the sources queue
    while sources:
        # more than one sequence mean, there is more than one way to reconstruct the sequence
        if len(sources) > 1:
            return False

        if oringinal_seq[len(sorted_order)] != sources[0]:
            # the next sources(or number) is different from the original sequence
            return False

        node = sources.popleft()
        sorted_order.append(node)

        for child in graph[node]:
            in_degrees[child] -= 1

            if in_degrees[child] == 0:
                sources.append(child)

    # if sorted order's size is not equal to original sequence's size, there is no unique way to construct
    return len(sorted_order) == len(oringinal_seq)


print(reconstruct_sequence([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]))
