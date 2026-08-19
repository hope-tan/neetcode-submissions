class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        buckets = [[] for i in range(len(nums) + 1)]
        for n, c in counter.items():
            buckets[c].append(n)

        results = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                results.append(n)
                if len(results) == k:
                    return results


