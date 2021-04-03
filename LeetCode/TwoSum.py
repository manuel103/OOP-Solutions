"""
Worst case scenario with runtime of O(n2)
"""

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for num1 in range(len(nums)):
#             for num2 in range(num1+1, len(nums)):
#                 if nums[num1] + nums[num2] == target:
#                     return [num1, num2]


"""
Worst case scenario with runtime of O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        ans = []
        for index in range(len(nums)):
            num2 = target - nums[index]
            if num2 in dict.keys():
                num2Index = nums.index(num2)
                if index != num2Index:
                    return sorted([index, num2Index])
                dict.update({nums[index]: index})

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
ans = solution.twoSum(nums, target)
print(ans)
