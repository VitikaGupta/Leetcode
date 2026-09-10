class Solution:
    def convertToBase7(self, num: int) -> str:
        b=""
        if num<0:
            b="-"
            num=-num
        if num==0:
            return "0"
        a=""
        while num>0:
            digit = num%7
            a+=str(digit)
            num//=7
        a=a[::-1]
        
           

        return b+a
            

        