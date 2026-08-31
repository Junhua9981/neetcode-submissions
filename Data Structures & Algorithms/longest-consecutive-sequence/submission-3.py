class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set(nums)
        ans = 0
        for a in s:
            if a-1 in s:
                continue
            b = a + 1
            while b in s:
                b = b+1
            
            ans = max(ans, b-a)
        return ans