class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while l < r :
                if nums[i] + nums[l] + nums[r] == 0:
                    triplets = [nums[i] , nums[l] , nums[r]]
                    if triplets in res:
                        l += 1
                    else:
                        res.append(triplets)
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0 :
                    r -= 1
                else:
                    l += 1
        return res