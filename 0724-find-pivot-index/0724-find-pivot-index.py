class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_sum = 0
        for i,e in enumerate(nums):
            if left_sum == s - left_sum - e:
                return i
            left_sum += e
        return -1