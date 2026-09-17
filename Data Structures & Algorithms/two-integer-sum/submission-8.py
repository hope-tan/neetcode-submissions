class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # see if we've seen a value that is target-value before
        # hashmap gives O(1) lookups
        # add values to hashmap each iteration and check target-i
        check = {}
        for index, value in enumerate(nums):
            if (target - value) in check:
                return [check[target - value], index]
            check[value] = index
        return []