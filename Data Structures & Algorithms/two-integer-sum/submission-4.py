class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 1 loop:
        #     diff = target - current
        #     look this^ up in hashmap.
        #     if yes, return [pair]
        #     if no, add current:index to hashmap and continue

        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
            
