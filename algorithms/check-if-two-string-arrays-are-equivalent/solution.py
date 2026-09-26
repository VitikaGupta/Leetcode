class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        a=" "
        b=" "
        for i in word1:
            a+=i
        for i in word2:
            b+=i
        if a==b:
            return True
        else:
            return False    
        