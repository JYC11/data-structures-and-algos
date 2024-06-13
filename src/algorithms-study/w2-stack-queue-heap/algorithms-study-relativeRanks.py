class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:

        sorted_score = sorted(score, reverse=True)

        hashmap = {}

        if len(score) > 2:
            hashmap[sorted_score[0]] = "Gold Medal"
            hashmap[sorted_score[1]] = "Silver Medal"
            hashmap[sorted_score[2]] = "Bronze Medal"

        elif len(score) == 1:
            return ["Gold Medal"]

        else:
            if score[0] > score[1]:
                return ["Gold Medal", "Silver Medal"]
            else:
                return ["Silver Medal", "Gold Medal"]

        rank = 4
        for index in range(3, len(sorted_score)):
            hashmap[sorted_score[index]] = str(rank)
            rank += 1

        return [hashmap[x] for x in score]
