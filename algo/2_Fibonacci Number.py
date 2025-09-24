from functools import lru_cache

class Solution(object):
    @lru_cache(maxsize=None)
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            answer = self.fib(n - 1) + self.fib(n - 2)
            return answer

solution = Solution()
result = solution.fib(6)
print(result)