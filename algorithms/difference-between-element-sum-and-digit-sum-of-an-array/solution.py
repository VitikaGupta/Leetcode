class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=0
        for i in nums:
            element_sum+=i
        l=[]
        for i in nums:
            for j in str(i):
                l.append(int(j))
        digit_sum=0
        for k in l:
            digit_sum+=k
        a=abs(element_sum-digit_sum)    
        return a



        