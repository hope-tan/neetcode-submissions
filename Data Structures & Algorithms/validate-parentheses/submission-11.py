class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        # list, append/pop takes O(1)
        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                stack.append(c)
            
            elif c == ")":
                if (stack and stack[-1] == "("):
                    stack.pop()
                else:
                    return False
            elif c == "]":
                if (stack and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if (stack and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True



