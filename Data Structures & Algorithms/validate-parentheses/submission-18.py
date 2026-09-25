class Solution:
    def isValid(self, s: str) -> bool:
        # make hashmap mapping close brackets to open brackets
        # if item is open bracket, append
        # if next item is close bracket
            # if stack has the matching open bracket, pop
            # if no matching bracket, return False
        # return True if stack is empty at end
        stack = []
        match = {")" : "(", "]":"[", "}":"{"}

        for c in s:
            if c in match:
                if (stack and match[c] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        if stack:
            return False
        else:
            return True