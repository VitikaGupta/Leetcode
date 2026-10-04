class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        nums=''.join(map(str,nums))
        digit=str(digit)
        count = 0
        for i in nums:
            if i==digit:
                count+=1
        return count

        