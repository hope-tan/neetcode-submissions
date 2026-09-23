class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # have 2nd data structure that you use to track values
        # iterate through nums
        # if value in nums is already in set, return true

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False