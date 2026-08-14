class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for s in range(len(stones)):
            if stones[s] in jewels:
             count += 1
        return count

        