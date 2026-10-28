class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        balance = 0
        for i in s:
            if i=='R':
                balance+=1
            else:
                balance-=1
            if balance ==0:
                count+=1
        return count


            
        