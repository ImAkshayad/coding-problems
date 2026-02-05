# Solution 1: With Sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            result[sorted_str].append(s)
        return list(result.values())
    
# Solution 2: Hash Table

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())
