class Solution(object):
    def convertDateToBinary(self, date):
        date = date.split('-')
        a = int(date[0])
        b = int(date[1])
        c= int(date[2])
        d = bin(a)[2:] + '-' + bin(b)[2:] + '-' + bin(c)[2:]
        return d
        
        