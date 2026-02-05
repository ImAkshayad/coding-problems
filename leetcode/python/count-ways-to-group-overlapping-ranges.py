class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        pre = -1
        result = 0
        for start, end in sorted(ranges):
            result += pre < start
            pre = max(pre,end)
        return pow(2,result,10**9+7)