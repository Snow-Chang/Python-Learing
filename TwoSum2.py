# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:07:01 2018
其他人的例子，运行时间36ms
@author: 常雪峰
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in table:
                return [table[diff], i]
            table[x] = i
if __name__=='__main__':
    nums = [3,2,4]
    Num = Solution().twoSum(nums,6)
    print(Num)