# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:04:05 2018
两数之和，最简单版本，运行时间过长
@author: 常雪峰
"""

class Solution():

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = len(nums)
        for i in range(0,L-1):
            for j in range(i+1,L):
                if (nums[i]+nums[j])==target:
                    return [i,j]
        print('没有两个数之和等于target')
    
        
    
if __name__=='__main__':
    d = Solution();
    Num = d.twoSum([2,7,11,15],9)
    print(Num)