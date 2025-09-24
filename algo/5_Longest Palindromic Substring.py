class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Нечётный палиндром (центр один символ)
            p1 = expand(i, i)
            if len(p1) > len(longest):
                longest = p1

            # Чётный палиндром (центр между двумя символами)
            p2 = expand(i, i + 1)
            if len(p2) > len(longest):
                longest = p2

        return longest

solution = Solution()
result = solution.longestPalindrome("abbafabba")
print(result)

