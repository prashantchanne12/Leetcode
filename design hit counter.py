'''
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.
'''

class HitCounter:
    
    def __init__(self):
        self.hits = []
    
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
    
    def getHits(self, timestamp: int) -> int:
        left = 0
        right = len(self.hits) - 1
        
        target = timestamp - 300
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.hits[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
        
        return len(self.hits) - left
    