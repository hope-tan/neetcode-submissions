class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams into sublists, return
        # hashmap sorted str: list of anagrams
        # return the values
        hashmap = {}
        for s in strs:
            sort = tuple(sorted(s))
            if sort in hashmap:
                hashmap[sort].append(s)
            else:
                hashmap[sort] = [s]
        return list(hashmap.values())