class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while l < r:
            area = (r-l) * max(height[l],height[r])
            res = max(res,area)
