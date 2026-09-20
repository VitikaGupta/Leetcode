class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        l=[]
        for ch in accounts:
            sum=0
            for i in ch:
                sum+=i
            l.append(sum)
        max=0
        for i in l:
            if i>max:
                max=i
        return max      
                
       