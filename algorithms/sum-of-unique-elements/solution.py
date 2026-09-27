class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d={}
        for ch in nums:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        l=[]
        for key,value in d.items():
            if value==1:
                l.append(key)
        sum=0
        for i in l:
            sum+=i
        return sum        

        