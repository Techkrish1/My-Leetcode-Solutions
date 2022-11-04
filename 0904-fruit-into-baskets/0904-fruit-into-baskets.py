class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_pick = 0
        left = 0
        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right],0) + 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            max_pick = max(max_pick , right - left + 1)
        return max_pick