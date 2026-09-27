import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make frequency map
        # get empty min heap of size k
        # pop when heap size is larger than k
        # return the heap
        count = {}
        heap = []
        result = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for v in count.keys():
            heapq.heappush(heap, (count[v], v))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
