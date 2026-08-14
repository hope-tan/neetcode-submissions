class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # outcome: return k most frequent integers in array nums

        # option 1
        # array of size n to track occurances of each value
        # traverse array to find highest number and return it

        # OR

        # option 2
        # group numbers based off their frequency 0-n
        # buckets where indices = frequency count
        # values = ints that occur at that frequency
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # use values as keys, keys as values
        for n, c in count.items():
            buckets[c].append(n)
        
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result


