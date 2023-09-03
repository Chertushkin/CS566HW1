# -*- coding: utf-8 -*-
"""CS566HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vg6X5VK6ehXjJYDRpDWuR6DGZCkB700y

## Homework 1. Introduction to algorithms

## Task 1. Solve the problem "Contains duplicate" from https://leetcode.com/problems/contains-duplicate/ using Python3

Use the box below, to paste the working code. The format of the code should be identical to LeetCode platform. (4 points)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TODO: implement your solution 

"""### Do not modify the testing code below. If you get message "Mistake in test case #", it means that you algorithm is incorrect."""

#test_case_1
expected, nums = True, [1,2,3,1]
actual = Solution().containsDuplicate(nums)
assert expected==actual, "Mistake in test case 1"

#test_case_2
expected, nums = False, [1,2,3,4]
actual = Solution().containsDuplicate(nums)
assert expected==actual, "Mistake in test case 2"

#test_case_3
expected, nums = True, [1,1,1,3,3,4,3,2,4,2]
actual = Solution().containsDuplicate(nums)
assert expected==actual, "Mistake in test case 3"

"""### Write analysis of the Memory Complexity and Time Complexity using Aymptotic Notation O. (1 point)

Memory Analysis: O - fill your details

Time Analysis: O - fill your details
"""