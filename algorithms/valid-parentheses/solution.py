class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        l=list(d.values())
        a=set(l)
        if len(a)==1:
            return True
        else:
            return False    
                
        