class Solution:
    def maxArea(self, height: List[int]) -> int:
        rs = 0
        start, end = 0, len(height) - 1
        while start < end:
            rs = max(rs, (end - start) * min(height[start], height[end]))
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        
        return rs
