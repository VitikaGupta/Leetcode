class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d={}
        for ch in nums:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        for key ,value in d.items():
            if value==1:
                return key

        