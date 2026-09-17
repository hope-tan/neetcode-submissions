class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force compare if a value at nums[i] has any corresponding value nums[j] that equals the target
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []