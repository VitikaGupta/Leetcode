class Solution(object):
    def maxFreqSum(self, s):
        d={}
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        vowels = "aeiou"        
        max_vowel =0
        max_con = 0
        for key,value in d.items():
            if key in vowels:
                max_vowel = max(max_vowel, value)
            else:
                max_con = max(max_con , value) 
        a=(max_vowel+max_con)
        return a
       


        