class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if "ba" not in s:
                return True
            else:
                return False    

        