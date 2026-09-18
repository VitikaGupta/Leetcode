class Solution:
    import string 
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        
        for i in string.punctuation:
            paragraph=paragraph.replace(i," ")
        paragraph=paragraph.lower()
        paragraph=paragraph.split()

        
        d={}
        for ch in  paragraph :
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        max_c=0
        a=""        
        for key,value in d.items():
            if key not in banned:
                if value > max_c:
                    max_c = value
                    a=key
        return a            

        