class Solution(object):
    def get_char_count(self, x):
        char_count = {}
        for i in x:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
        return char_count
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_char_count = self.get_char_count(s)
        t_char_count = self.get_char_count(t)
        
        return s_char_count == t_char_count
        