class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        di=0
        sum=0
        pro=1
        while n>0:
            digit=n%10
            sum+=digit
            pro=pro*digit
            n//=10

        di=pro-sum
        return di

