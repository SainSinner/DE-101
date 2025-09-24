class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix
solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)
#
# variable = ["flower","flow","flight"]
# print(variable[1][1])