class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        value = 0
        for s in strs:
            if s.isnumeric():
                value = max(value, int(s))
            else:
                value = max(value, len(s))
        return value