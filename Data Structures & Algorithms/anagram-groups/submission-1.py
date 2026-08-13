class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # strs is a list of strings
        # hashmap where key is sorted tuple
        # values are the words that are anagrams
        # of the tuple
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())