import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate through and store stuff in a hashmap
        # value : # of appearances
        # sort by # of appearances
        # pop and append top K values in hashmap

        hashmap = {}
        result = []

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
            
        sorted_hashmap = dict(sorted(hashmap.items(), key = lambda item:item[1]))
        
        for i in range(k):
            key, value = sorted_hashmap.popitem()
            result.append(key)

        return result

