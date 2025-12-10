class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        a = 2
        b = 3

        for _ in range(3,n):
            current = a + b
            a = b
            b = current
        return current