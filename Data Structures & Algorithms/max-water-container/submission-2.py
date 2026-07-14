class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_of_heights = len(heights)

        left = 0
        right = len_of_heights-1

        mx_area = 0
        # return [left, right]
        # return [heights[left], heights[right]]
        while left < right:
            
            cur_height = min(heights[left], heights[right])
            cur_width = right - left

            cur_area = cur_height * cur_width
            mx_area = max(mx_area, cur_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return mx_area