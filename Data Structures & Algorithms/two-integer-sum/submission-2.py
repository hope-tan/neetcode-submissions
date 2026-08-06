class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through nums using for loop
        # for each int in nums, loop through nums again to see if the values add up
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return[i, j]