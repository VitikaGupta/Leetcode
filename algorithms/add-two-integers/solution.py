class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini=nums.index(min(nums))
        maxi=nums.index(max(nums))
        i=min(mini,maxi)
        j=max(maxi,mini)
        front = j+1
        back=len(nums)-i
        both=(i+1)+(len(nums)-j)
        a=min(front,back,both)
        return a


        