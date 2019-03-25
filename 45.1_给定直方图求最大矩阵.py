"""
给定一个直方图中每一竖列的高度
如：4 3 2 5 6 表示的是从左向右高度分别为4,3,2,5,6的一个直方图
求这个直方图整体中最大的的矩形的面积

思路：
以0位置的4为例 向左看能不能扩 能扩的条件为左边的高度比他小
由于4左边没有数列 而右边的3又比他小 所以0位置的4不能扩
以1位置的3为例 左边的4比他大 因此他可以向左扩
右边的2比他小 所以不能向右扩 那么1位置的3能扩出来的最大面积为2x3=6
以此类推
"""

# TODO 给定直方图求最大矩阵
# 先构建一个栈底到栈顶为由小到达的单调栈
# 原先是求离他最近比他大的 现在求离他最近比他小的

from queue import LifoQueue


class BasicNode(object):
    def __init__(self, index, elem):
        self.index = index
        self.elem = elem
        self.next = None
        self.lSmaller = None
        self.rSmaller = None
        self.maxHigh = 0


class CreateStack(object):
    def __init__(self, arr):
        self.arr = arr
        self.q = LifoQueue()
        self.index = 0
        self.length = len(arr)

    def getMax(self):
        newNode = BasicNode(self.index, self.arr[self.index])
        self.q.put(newNode)
        self.index += 1
        for _ in range(self.length):
            newNode = BasicNode(self.index, self.arr[self.index])
            curNode = self.q.get()
            if curNode.elem < newNode.elem:
                self.q.put(curNode)
                self.q.put(newNode)
                newNode.lSmaller = curNode
            elif curNode.elem > newNode.elem:
                # 此时的curNode是因为newNode的到来而弹出的
                # 还要考虑数字相同的情况
                # if curNode.lSmaller is None:
                #     curNode.maxHigh = curNode.elem * (curNode.index - (-1))
                #     self.q.put(newNode)
                # else:
                #     while curNode.lSmaller is not None and not self.q.empty():
                #         curNode.maxHigh = (self.length - curNode.index) * curNode.elem
                #         curNode = self.q.get()
                #     curNode.maxHigh = self.length
                while not self.q.empty():
                    helpIndex = curNode.index
                    if curNode.lSmaller is None:
                        curNode.maxHigh = curNode.elem * (curNode.index - (-1))

            else:
                curNode.next = newNode
                self.q.put(curNode)
                self.q.put(newNode)
