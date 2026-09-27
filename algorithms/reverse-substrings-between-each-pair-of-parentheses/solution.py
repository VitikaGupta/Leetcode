class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        a=""
        for ch in s:
            if ch=='(':
                stack.append(a)
                a=""
            elif ch ==')':
                a=a[::-1]
                a=stack.pop()+a
            else:
                a+=ch
        return a    

        