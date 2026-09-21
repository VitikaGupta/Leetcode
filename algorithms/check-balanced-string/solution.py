class Solution:
    def isBalanced(self, num: str) -> bool:
        l1=[]
        l2=[]
        for i in range(len(num)):
            if i%2==0:
                l1.append(num[i])
            else:
                l2.append(num[i])
        sum1=0
        for i in l1:
            sum1+=int(i)
        sum2=0
        for i in l2:
            sum2+=int(i)
        if sum1==sum2:
            return True
        else:
            return False                     

        