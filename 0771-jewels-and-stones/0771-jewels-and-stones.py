class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for i in jewels:
            c = stones.count(i)
            res += c
        return res