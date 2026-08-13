class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check lengths are equal
        if len(s) != len(t):
            return False
        
        # initalize hashmaps that count occurances
        # of each occurance of a letter
        countS, countT = {}, {}
        
        # add up how many occurances of each
        # letter appear in s and t
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # s and t are anagrams if s and t are equal
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
        