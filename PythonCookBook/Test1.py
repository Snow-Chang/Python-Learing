# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 08:16:12 2018
解压序列值付给多个变量
@author: 常雪峰
"""
'''
任何序列可以通过一个简单的赋值语句解压
'''
p = (4,5)
x,y = p
# 
data = ['ACME',50,91.11,(2012,10,12)]
name,shares,price,(year,mon,day) = data
# 只想解压一部分可以用任意变量名_占位
_，shares,price,_ = data

# 也可以解压可迭代对象
# *表达式
name, *sh,time, = data
# collection.deque 双端队列
# 在多行上进行文本匹配
# 只保存最后的几个记录，即把最早的记录弹出
from collection import deque 

def serch(lines,pattern,history=5):
    previous_lines = deque(maxlen = history)
    for li in lines:
        if pattern in li :
            yield li, previous_lines # 生成器函数
        previous_lines.append(li)

# Example on a file 
if __name__ = '__main__':
    with open ('cookbook.txt') as f:
        for line, prevlines in search(f,'python',5):
            for pline in prevlines:
                print (pline,end = '')
            print (line,end = '')
            print('_'*20)
            
# heap 模块 堆排序模块
# 字典中的键映射多个值