class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stored = set()
        longest = 0
        left = 0
        for right in range(len(s)):
            while s[right] in stored:
                stored.remove(s[left])
                left +=1
            stored.add(s[right])
            longest = max(longest , right - left + 1)
        return longest
                