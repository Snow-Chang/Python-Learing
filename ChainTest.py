# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:52:03 2018
用Python模拟链表，实现了链表的插入，删除等操作
@author: Administrator
"""

class Node:
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象
    '''
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.data)
    
    
class Chain():
    '''
    
    '''
    def __init__(self):
        self.length = 0
        self._head = None
        
    def isEmpty(self):
        return self.length == 0
    
    def append(self,item):
        if isinstance(item,Node):
            node = item
        else:
            node = Node(item)
        
        if self._head == None:
            self._head= node
        else :
            Nodetmp = self._head
            while Nodetmp._next:
                Nodetmp = Nodetmp._next;
            Nodetmp._next = node
        self.length += 1

    def insert(self, index, item):
        
        if self.isEmpty():
            print('this chain is empty')
            return
        
        if index<0 or index> self.length:
            print('error: out of index')
            return
        
        if isinstance(item,Node):
            nodein = item
        else:
            nodein = Node(item)
            
        node = self._head
        count = 0
        
        while True:
            node = node._next
            count += 1
            if count == index:
                next_node = node._next
                node._next = nodein
                nodein._next = next_node
                self.length+=1
                return
            
    def delete(self,index):
        
        if self.isEmpty():
            print('this chain is empty')
            return
        
        if index<0 or index> self.length:
            print('error: out of index')
            return
        
        node = self._head
        count = 0
        while True:
            count += 1
            if index == count:
                node._next = node._next._next
                break
            node = node._next
        self.length -= 1
    
    def __repr__(self):
        if self.isEmpty():
            print("the chain table is empty")
            return
        nlist = ""
        node = self._head
        while node:
            nlist += node.data +''
            node = node._next
        return nlist
                
if __name__ == '__main__':
    chain = Chain()
    chain.append('A')
    chain.append('B')
    chain.append('C')
    chain.append('D')
    chain.append('E')
    chain.append('F')
    chain.append('G')
    chain.insert(4,'p')
    chain.delete(1)
    print(chain,chain._head.data,chain.length)
            