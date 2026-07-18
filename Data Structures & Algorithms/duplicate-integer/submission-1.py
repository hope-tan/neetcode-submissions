class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through nums
            # check: is num inside of hash set already?
                # yes: return True
                # no: keep going and add it to the hash set

        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False