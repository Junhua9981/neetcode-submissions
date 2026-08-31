class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1,]
        subfix = [1,]
        p = 1
        s = 1

        for i in range(len(nums)):
            p = p * nums[i]
            prefix.append(p)
            s = s * nums[len(nums)-i-1]
            subfix.append(s)
        ans = []

        for i in range(len(nums)):
            ans.append(prefix[i]*subfix[len(nums)-i-1])
        return ans