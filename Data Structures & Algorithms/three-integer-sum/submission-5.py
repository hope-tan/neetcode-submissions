class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # store all elements in hashmap of value : indices and sort it
        # for any unique number, there are 2 numbers that will make it = 0
        # e.g. 3 can be made 0 with [-3, 0], [-1, -2], [-5, 2]
        # for each number nums[i] then use 2 ptrs to check if 2 other values summed together equal -nums[i] to equal 0
        hashmap = {} # int:list
        result = []
        for i, v in enumerate(nums):
            hashmap.setdefault(v, []).append(i)
        
        sortedMap = sorted(hashmap)

        for index, i in enumerate(sortedMap):
            for j in sortedMap[index:]:
                k = -(i + j)
                if k >= j and k in sortedMap:
                    if (i == j and i != k and len(hashmap[i])>= 2):
                        result.append([i, j, k])
                    elif (j == k and i != k and len(hashmap[j])>= 2):
                        result.append([i, j, k])
                    elif (i == j and i ==k and len(hashmap[i]) >= 3):
                        result.append([i, j, k])
                    elif (j!= k and i!=j and i!=k):
                        result.append([i, j, k])
        return result

