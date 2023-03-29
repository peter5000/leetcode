# https://leetcode.com/problems/two-sum/
# 3/26/2023

# 1. Two Sum
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [0,0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    answer[0] = i
                    answer[1] = j
                    return answer
        return answer

# Optimized solution

# Make a dictionary
# Iterate through the given list if complement of current number to target
# is in a dictionary, return the index of complement and current
# If not, store value of current number into a dictionary with an index

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         int_found = {}
#         for i in range(len(nums)):
#           if target - nums[i] in int_found:
#               return [int_found[target - nums[i]], i]
#           else:
#             int_found[nums[i]] = i
#         return []