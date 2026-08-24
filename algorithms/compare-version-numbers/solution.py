class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        d1=version1.split('.')
        d2=version2.split('.')
        n=max(len(d1),len(d2))
        for i in range(n):
            v1=int(d1[i])  if i <len(d1) else 0
            v2=int(d2[i])  if i <len(d2) else 0
            if v1>v2:
                return 1
            if v2>v1:
                return -1
        return 0        


        