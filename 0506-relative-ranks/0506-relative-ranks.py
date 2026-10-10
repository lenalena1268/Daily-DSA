class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        result = []
        score_sorted = sorted(score,reverse = True)
        ranks = {}
        for i in range(len(score_sorted)):
            if i == 0:
                ranks[score_sorted[i]] = "Gold Medal"
            elif i == 1 :
                ranks[score_sorted[i]] = "Silver Medal"
            elif i == 2:
                ranks[score_sorted[i]] = "Bronze Medal"
            else:
                ranks[score_sorted[i]] = str(i+1)

        for s in score:
            result.append(ranks[s])

        return result
        