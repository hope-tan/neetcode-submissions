class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        openClose = {")":"(", "]":"[", "}":"{"}
        # list, append/pop takes O(1)
        for c in s:
            if c in openClose:
                if stack and stack[-1] == openClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else: 
            return True