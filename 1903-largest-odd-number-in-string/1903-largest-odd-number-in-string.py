class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = 1
        while True:
            if i > len(num):
                return ""
                break
            n = num[-i]
            if n in '02468':
                i += 1
                continue
            elif n not in '02468':
                return (num[0:len(num)-i+1])
                break