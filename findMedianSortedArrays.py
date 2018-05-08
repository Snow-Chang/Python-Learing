# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:09:52 2018

@author: Administrator
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        while(len(nums1)+len(nums2)>2):
            if nums1 and nums2:
                if nums1[0]>nums2[0]:
                    del nums2[0]
                else:
                    del nums1[0]
            elif nums1:
                del nums1[0]
            else :
                del nums2[0]
            if nums1 and nums2:   
                if nums1[-1]>nums2[-1]:
                    del nums1[-1]
                else:
                    del nums2[-1]
            elif nums1:
                del nums1[-1]
            else :
                del nums2[-1]
            
        if (len(nums1)+len(nums2)==2):
            return (sum(nums1)+sum(nums2))/2
        return (sum(nums1)+sum(nums2))

if __name__ == '__main__':
    a=Solution().findMedianSortedArrays([1,3],[2,5])
    print(a)