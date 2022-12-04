class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence
        for i in range(len(s)):
            if s[i] == " " and s[i-1] != s[i+1]:
                return False
        return s[0] == s[-1]