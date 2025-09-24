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