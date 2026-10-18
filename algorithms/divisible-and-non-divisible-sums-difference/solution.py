class Solution(object):
    def differenceOfSums(self, n, m):
        l=[]
        l1=[]
        for i in range(1,n+1):
            if i%m==0:
                l.append(i)
            else:
                l1.append(i)
        num1=0    
        num2=0
        for i in l1:
            num1+=i
        for i in l:
            num2+=i
        d=num1-num2
        return d 


        
       
        