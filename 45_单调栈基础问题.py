"""
题目：
给定一个无序的数组 分别求每个数左边离他最近比它大的数和右边离他最近比它大的数
常规方法就是遇到一个数左边遍历右边也遍历 那么时间复杂度就为O(N^2)
现要求时间复杂度为0(N)解决这个问题

单调栈概念：
单调递增或单调减的栈

解题思路：
构造一个栈结构 这个栈结构为底部大顶部小的单调栈结构
将数组的数从头压入这个栈结构 压入的条件是准备压入的数比前一个数小
当压入的数比前一个数大的时候 进行弹出操作
此时弹出的数是因为这个数而弹出的 那么弹出的数右边离他最近比他大的就是这个将要压入的数
而左边离他最近比他大的就是下一个将要弹出的数
直到要弹出的数比这个将要压入的数大时重新开始压入操作
到最后没有数可压入的时候进行弹出操作
此时弹出的数不是因为别的数而弹出的 所以此时弹出的数右边离他最近比他大的数不存在
特殊情况：遇到相等的数的时候将坐标压入到同一层
"""
from queue import LifoQueue


class BaseNode(object):
    def __init__(self, index, elem):
        self.index = index
        self.elem = elem
        self.next = None
        self.lBigger = None
        self.rBigger = None


class GetFreshNum(object):
    def __init__(self, arr):
        self.q = LifoQueue()
        self.arr = arr
        self.index = 0
        self.length = len(arr)
        self.helpArr = []

    def getNum(self):
        newNode = BaseNode(self.index, self.arr[self.index])
        self.q.put(newNode)
        self.index += 1
        while self.index < self.length:
            newNode = BaseNode(self.index, self.arr[self.index])
            curNode = self.q.get()
            # print(curNode.index)
            # print(curNode.elem)
            # print(self.index)
            if self.arr[self.index] < curNode.elem:
                newNode.lBigger = curNode
                self.q.put(curNode)
                self.q.put(newNode)
                # print('-' * 50)
                # print(self.q.qsize())
                # print('-' * 50)
                self.index += 1
            elif self.arr[self.index] == curNode.elem:
                curNode.next = newNode
                self.q.put(curNode)
                # print('=' * 50)
                # print(self.q.qsize())
                # print('=' * 50)
                self.index += 1
            else:
                # print(self.q.qsize())
                # newNode = BaseNode(self.index, self.arr[self.index])
                while curNode.elem < self.arr[self.index]:
                    curNode.rBigger = newNode
                    # print('text2')
                    self.helpArr.append(curNode)
                    curNode = self.q.get()
                    # print(curNode.elem)
                    if self.q.empty() and curNode.elem < self.arr[self.index]:
                        curNode.rBigger = newNode
                        self.q.put(newNode)
                        self.helpArr.append(curNode)
                        # print(newNode.index)
                        # print(self.q.qsize())
                        break
                # self.q.put(curNode)
                self.index += 1
        while True:
            # print('text3')
            self.helpArr.append(self.q.get())
            if self.q.empty():
                break

test = GetFreshNum([5, 4, 3, 6, 5, 3])
test.getNum()
for i in test.helpArr:
    print(str(i.elem) + ' and index is ' + str(i.index))
    print(i.lBigger if i.lBigger is None else str(i.lBigger.elem) + ' lBigger"s index is ' + str(i.lBigger.index))
    print(i.rBigger if i.rBigger is None else str(i.rBigger.elem) + ' rBigger"s index is ' + str(i.rBigger.index))