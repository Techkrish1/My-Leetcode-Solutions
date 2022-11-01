class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_pointer = right_pointer = 0
        while left_pointer < len(s) and right_pointer < len(t):
            if s[left_pointer] == t[right_pointer]:
                left_pointer += 1
            right_pointer += 1
        return left_pointer == len(s)
        