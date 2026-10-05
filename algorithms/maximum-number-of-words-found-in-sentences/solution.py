class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        l=[]
        for i in sentences:
            j=i.split()
            l.append(len(j))
        max=0
        for i in l:
            if i > max :
                max=i
        return max

