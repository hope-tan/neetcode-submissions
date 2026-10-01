class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # increasing order
        # return 1-indexed indices of 2 nums that add up to target
        # solution must be O(1) space
        l = 0
        r = len(numbers)-1
        
        while l < r:
            # check if l + r is target, otherwise keep decrementing r
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l +=1
            else:
                r -= 1
