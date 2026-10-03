class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            elif ch=="*":
                stack.pop()
        a=''.join(stack)
        return a

        