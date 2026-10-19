class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        return l


        
        