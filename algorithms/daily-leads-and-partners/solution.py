class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums)
        l=[]
        for i in range(1,n+1):
            if n%i==0:
                l.append(nums[i-1])
        sum = 0
        for i in l:
            sum+=i*i
        return sum


       
        