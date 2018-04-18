# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:12:33 2018

@author: Administrator
"""

def gcd (p,q):
    if q==0:
        return p
    else:
        r=p % q
        return gcd(q, r)
