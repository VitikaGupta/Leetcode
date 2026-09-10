class Solution:
    def countCommas(self, n: int) -> int:
        count=0
        if n>=1000:
            count+=min(n,999999)-1000+1
        if n>=1000000:
            count+=(min(n,999999999)- 1000000 +1)*2
        if n>=1000000000:
            count+=(min(n,999999999999)- 1000000000+1)*3  
        if n >= 1000000000000:
            count += (min(n, 999999999999999) - 1000000000000 + 1) * 4

        if n >= 1000000000000000:
             count += 1 * 5
        return count     

      