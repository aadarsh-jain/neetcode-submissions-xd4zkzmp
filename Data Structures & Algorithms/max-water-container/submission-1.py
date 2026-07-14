class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_heights = len(heights)
        res = 0
        for i in range(len_heights):
            for j in range(i + 1, len_heights):
                amount = min(heights[i], heights[j]) * (j - i)
                if res < amount:
                    res = amount
        return res