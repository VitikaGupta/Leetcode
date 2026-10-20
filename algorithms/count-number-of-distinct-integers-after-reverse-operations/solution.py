class Solution(object):
    def countDistinctIntegers(self, nums):
        l=[]
        for i in range(len(nums)):
            a=int(str(nums[i])[::-1])
            l.append(a)
        b=nums+l
        c=set(b)
        return len(c)

        