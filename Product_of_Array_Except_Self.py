# https://leetcode.com/problems/product-of-array-except-self/
# 3/28/2023

# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal
# to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = nums.copy()
        suffix_product = nums.copy()
        for i in range(1,len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i]
        for i in range(len(nums)-2,-1,-1):
            suffix_product[i] = suffix_product[i+1] * nums[i]
        answer = []
        answer.append(suffix_product[1])
        for i in range(1,len(nums)-1):
            answer.append(prefix_product[i-1]*suffix_product[i+1])
        answer.append(prefix_product[len(nums)-2])
        return answer