class Solution(object):
    def findRelativeRanks(self, score):
        sorted_score = sorted(score , reverse = True)
        l=[]
        for s in score:
            rank = sorted_score.index(s)+1
            if rank == 1:
                l.append("Gold Medal")
            elif rank== 2:
                 l.append("Silver Medal")
            elif rank == 3:
                 l.append("Bronze Medal")
            else:
                l.append(str(rank))
        return l
