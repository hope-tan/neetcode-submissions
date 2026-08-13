class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # strs is a list of strings
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())