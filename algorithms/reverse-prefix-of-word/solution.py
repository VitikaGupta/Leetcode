class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            sum=0
            while i>0:
                sum+=i%10
                i//=10
            l.append(sum)

        a=-1
        for i in range(len(l)):
            if i==l[i]:
                a=i
                break
        return a           
        