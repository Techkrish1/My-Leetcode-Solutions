class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        jewels = set(jewels) # search in a set is instant - O(1)
        for stone in stones:
            if stone in jewels:
                counter += 1
        return counter