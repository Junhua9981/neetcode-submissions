class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = -1

        while l < r:
            sz = (r - l) * min(heights[l], heights[r])
            ans = max(ans, sz)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans
