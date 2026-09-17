class Solution:
    def sumOfMultiples(self, n: int) -> int:
        l=[]
        for i in range(1,n+1):
            if i%3==0 ==0 or i%5==0 or i%7==0:
                l.append(i)
        sum=0
        for i in l:
            sum+=i
        return sum            

        