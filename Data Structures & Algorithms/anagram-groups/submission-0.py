class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)

        for s in strs:
            d["".join(sorted(s))].append(s)
        ans = []
        for k, v in d.items():
            ans.append(v)
        return ans