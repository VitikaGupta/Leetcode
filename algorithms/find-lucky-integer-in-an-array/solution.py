class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for ch in arr:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        a=-1        
        for key,value in d.items():
            if key==value :
                a=max(key,a)
        return a       
            