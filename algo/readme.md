### Пузырьковая сортировка

```python
def sorted_array(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    answer = array
    return answer


nums = [5, 2, 9, 1, 5, 6]
print(sorted_array(nums))
```

### Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer = [i, j]
                    return answer

solution = Solution()
result = solution.twoSum([3,2,4], 6)
print(result)
```

### Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

```python
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
```

### Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 0
        answer = []
        is_zero_array = False
        for i in range(len(nums)):
            if nums[i] != 0:
                if product == 0:
                    product = nums[i]
                else:
                    product = product * nums[i]
            else:
                is_zero_array = True
        for j in range(len(nums)):
            if is_zero_array == True and nums[j] != 0:
                answer.append(0)
            if is_zero_array == True and nums[j] == 0:
                answer.append(product)
            if is_zero_array == False and nums[j] != 0:
                answer.append(int(product/nums[j]))
        return answer

solution = Solution()
result = solution.productExceptSelf([0,0])
print(result)
```

### Longest Common Prefix
GWrite a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
```python
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
```

### Longest Common Prefix
Given a string s, return the longest palindromic substring in s.

```python
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
```
