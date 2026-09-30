class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        sum_odd = n*n
        sum_even = n*(n+1)
        g= math.gcd(sum_odd,sum_even)
        return g
        
        