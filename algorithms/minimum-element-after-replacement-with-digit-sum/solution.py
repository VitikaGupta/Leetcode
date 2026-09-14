class Solution:
    def minElement(self, nums):
        ans = []

        for num in nums:
            total = 0

            for digit in str(num):
                total += int(digit)

            ans.append(total)

        return min(ans)