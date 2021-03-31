from heapq import *


class MedianOfStream:

    # cotains first half of numbers
    maxHeap = []
    # contains second half of numbers
    minHeap = []

    def insert_num(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # either both heaps will have equal number of elements or max-heap will have more elements than min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            # we have even number of elements, take the average of middle two elements
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

        # because max-heap will have one more element than the min-heap
        return -self.maxHeap[0] / 1.0


def main():
    medianOfStream = MedianOfStream()
    medianOfStream.insert_num(3)
    medianOfStream.insert_num(1)
    print('The median is: '+str(medianOfStream.find_median()))

    medianOfStream.insert_num(5)
    print('The median is: '+str(medianOfStream.find_median()))

    medianOfStream.insert_num(4)
    print('The median is: '+str(medianOfStream.find_median()))


main()
