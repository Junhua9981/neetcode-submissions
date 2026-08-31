import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)

        for i, n in enumerate(nums):
            if target-n != n and d[target-n]:
                return [i, d[target-n][0]]
            elif target-n == n and len(d[target-n])>=2:
                return d[target-n][:2]
        return -1