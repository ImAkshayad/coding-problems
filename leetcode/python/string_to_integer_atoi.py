class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        i = 0
        s = s.strip()
        if not s:
            return 0

        sign_ = 1
        if s[i] in ('+','-'):
            if s[i] == '-':
                sign_ = -1    
            i += 1
        
        res = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign_ == 1 else INT_MIN
            
            res = int(res * 10) + int(digit)
            i += 1
        return res * sign_




        