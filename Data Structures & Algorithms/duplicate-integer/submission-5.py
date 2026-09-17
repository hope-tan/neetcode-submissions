class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # use a hashset to track if a number is a repeat/occurs more than once
        # if number appears in hashset, return true
        # if number does not appear in hashset, add it to the hashset and move on
        # if you loop through everything and have no duplicates, return false

        hashset = set()
        
        for n in nums:
            
            if n in hashset:
                return True

            hashset.add(n)
        return False