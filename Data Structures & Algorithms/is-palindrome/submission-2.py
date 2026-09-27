import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # iterate through
            # if c is alphanumeric, add to new string
            # if not, skip
        # convert whole string to lowercase
        # if length % 2 == 1 return False
        # if length % 2 == 0 compare spot 0 with n, 1 with n-1
        # return outcome
        
        new = ""
        # an = set(string.ascii_letters + string.digits)
        for c in s:
            if c.isalnum():
                new += c.lower()
        print(new)
        return new == new[::-1]