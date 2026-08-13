class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hash table.
        # key is tuple derived from array of
        # frequency of occurance per letter.
        # value is strings that match.
        hashmap = {}

        # for every string
        for s in strs:
            # initalize an array of size 26 to count frequencies
            counter = [0] * 26
            
            # for each of the chars in the string,
            # add 1 to its frequency counter
            for c in s:
                counter[ord(c) - ord('a')] += 1

            # make the frequency array the key and the string the value
            hashmap.setdefault(tuple(counter), []).append(s)

        # return a list of the values
        return list(hashmap.values())
