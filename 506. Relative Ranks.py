class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        places = {0:"Gold Medal",1:"Silver Medal",2:"Bronze Medal"}
        new_score = sorted(score)[::-1]
        for i in range(len(new_score)):
            if i <= 2 :
                score[score.index(new_score[i])] = places[i]
            else :
                score[score.index(new_score[i])] = str(i+1)
        return score
        