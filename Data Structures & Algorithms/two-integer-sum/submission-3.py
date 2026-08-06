class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through nums using for loop
        # for each int in nums, loop through nums again to see if the values add up to the target
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]