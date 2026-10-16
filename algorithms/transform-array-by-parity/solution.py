class Solution(object):
    def sumCounts(self, nums):
        n=len(nums)
        sum=0
        for i in range(n):
            for j in range(i,n):
                a=nums[i:j+1]
                b=len(set(a))
                sum+=b**2
        return sum
        
        