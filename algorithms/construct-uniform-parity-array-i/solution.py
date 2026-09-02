class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(x%2==0 for x in nums1) or all (x%2 for x in nums1):
            return True
        else:
            nums2=[]
            for i in range(len(nums1)):
                for j in range(len(nums1)):
                    if i!=j:
                        a=nums1[i] - nums1[j]
                        if a%2!=0:
                            nums2.append(a)
                            break
            return True                


        