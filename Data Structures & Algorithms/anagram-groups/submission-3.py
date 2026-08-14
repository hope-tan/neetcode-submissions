class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # objective: group all anagrams into sublists
        # key: anagram sorted into alphabetical order
        # key2: array of size 26 where you count the number of occurances of each letter
            # array[0] = 2 means there are 2 occurances of a
        # value: list of anagrams
        hashmap = {}
        
        for s in strs:
            counter = [0] * 26

            for c in s:   
                counter[ord(c) - ord('a')] += 1

            key = tuple(counter)

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(s)

        return list(hashmap.values())