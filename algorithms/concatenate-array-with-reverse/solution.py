class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        num=nums[::-1]
        a=nums+num
        return a
        