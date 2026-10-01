class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={
            '(':')',
            '[':']',
            '{':'}'
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}":
                if not stack or d[stack[-1]]!=ch:
                    return False
                else:
                    stack.pop()    
        if len(stack)==0:
            return True
        else:
            return False    

        