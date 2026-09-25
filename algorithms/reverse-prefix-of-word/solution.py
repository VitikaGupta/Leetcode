class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=word
        for i in range(len(word)):
            if word[i]==ch:
                a=word[:i+1][::-1]+word[i+1:]
                break
        return a
           
        