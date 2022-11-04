class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        Max = float('inf')
        length = Max
        add = 0
        for right in range(len(nums)):
            add += nums[right]
            if add >= target:
                while add >= target:
                    length = min(length , right - left + 1)
                    add -= nums[left]
                    left += 1
        return 0 if length == Max else length