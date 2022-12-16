class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while l < r:
            area = (r-l) * max(height[l],height[r]) # width * minimum height
            res = max(res,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
         return(res)
