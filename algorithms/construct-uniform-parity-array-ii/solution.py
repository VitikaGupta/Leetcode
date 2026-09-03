class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(x%2==0 for x in nums1) or all(x%2 for x in nums1):
            return True
        min_odd = min(x for x in nums1 if x % 2 != 0)

        # Every even number must be greater than the smallest odd number
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True
       