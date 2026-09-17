class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if 2 strings are anagrams, return true
        # otherwise, return false
        # sort s and t so they are alphabetical
        # if s and t are the same, return true

        
        if len(s) != len(t): 
            return False
        return sorted(s) == sorted(t)