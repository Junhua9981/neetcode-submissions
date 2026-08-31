from bisect import bisect_left
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_dict = defaultdict(list)
        for i, n in enumerate(numbers):
            if hash_dict[target-n]:
                return [hash_dict[target-n][0]+1, i+1]
            hash_dict[n].append(i)

            
        return -1
