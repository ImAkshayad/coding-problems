class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            # Checks if duplicate character is present in any other indices
            # if not, function returns the index of first unique character
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        return -1