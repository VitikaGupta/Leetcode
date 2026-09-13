class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        for ch in str(n):
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1

        sum=0
        for key,value in d.items():
            sum+=int(key)*value
        return sum        
                    