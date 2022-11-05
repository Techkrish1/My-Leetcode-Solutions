class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d_jewels = dict()
        for i in jewels:
            d_jewels[i] = d_jewels.get(i,0) + 1
        old_sum = sum(d_jewels.values())
        for i in stones:
            if i in d_jewels:
                d_jewels[i] = d_jewels.get(i,0) + 1
        return sum(d_jewels.values()) - old_sum