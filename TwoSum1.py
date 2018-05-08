# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:38:11 2018
第二个方案，运行时间1392ms
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
        if L==1:
            print('error : length of  nums <2')
        for i in range(0,L):
                if target-nums[i] in nums:
                    j = nums.index(target-nums[i])
                    if(i!=j):
                        return [i,j]
        print('没有两个数之和等于target')
    
        
    
if __name__=='__main__':
    nums = [3,2,4]
    Num = Solution().twoSum(nums,6)
    print(Num)