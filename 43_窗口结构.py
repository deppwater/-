"""
一个窗口有如下功能：
左边界右移即窗口大小减小的功能 右边界右移即窗口大小增大的功能
获取当前窗口中的最大值的功能

实现细节：
实现一个双向链表 将窗口中的数据的index从左到右依次加入该双向链表
如果先加入的值小于等于新加入的值 那么弹出先加入的值直到该双向链表最左边的值是整个链表中最大的为止
如果窗口增大 则重复上述操作
如果窗口减小 则弹出链表中对应于原数据index的数据 如果不存在则不进行操作
需要注意的是窗口左边界不能超过右边界
"""


class Node(object):
    def __init__(self, index, elem):
        self.elem = elem
        self.index = index
        self.next = None
        self.pre = None


class Window(object):
    def __init__(self, arr, qMin, qMax):
        self.arr = arr
        self.qMin = qMin
        self.qMax = qMax
        self.head = None
        self.last = None
        self.makeWindow()

    def makeWindow(self):
        """初始化窗口"""
        self.head = Node(0, self.arr[self.qMin])
        self.last = self.head
        curNode = self.head
        # print(curNode)
        for i in range(self.qMin + 1, self.qMax + 1):
            # print(curNode.elem)
            if self.arr[i] < curNode.elem:
                newNode = Node(i, self.arr[i])
                self.last = newNode
                curNode.next = newNode
                newNode.pre = curNode
                curNode = newNode
            else:
                newNode = Node(i, self.arr[i])
                if self.arr[i] >= self.head.elem:
                    self.head = newNode
                    self.last = newNode
                    curNode = newNode
                    # print('text')
                else:
                    # print('text')
                    # print(curNode.elem)
                    # print(curNode.pre.elem)
                    while curNode.elem <= self.arr[i] and curNode.pre is not None:
                        curNode.elem = self.arr[i]
                        curNode.index = i
                        curNode.next = None
                        self.last = curNode
                        curNode = curNode.pre
                    curNode = curNode.next
                    # print(curNode.elem)

    def getMax(self):
        return self.head

    def extendWindow(self):
        curNode = self.last
        self.qMax += 1
        curIndex = self.qMax
        if curIndex > len(self.arr) - 1:
            return '超过边界'
        if self.arr[curIndex] < curNode.elem:
            newNode = Node(curIndex, self.arr[curIndex])
            self.last = newNode
            curNode.next = newNode
            newNode.pre = curNode
        else:
            newNode = Node(curIndex, self.arr[curIndex])
            if self.arr[curIndex] >= self.head.elem:
                self.head = newNode
                self.last = newNode
                # print('text')
            else:
                # print('text')
                # print(curNode.elem)
                # print(curNode.pre.elem)
                while curNode.elem <= self.arr[curIndex] and curNode.pre is not None:
                    curNode.elem = self.arr[curIndex]
                    curNode.index = curIndex
                    curNode.next = None
                    self.last = curNode
                    curNode = curNode.pre

    def reduceWindow(self):
        # print('text')
        if self.qMax == self.qMin:
            # print('text')
            return '不能进行缩小操作'
        self.qMin += 1
        if self.qMin <= self.head.index:
            # print(self.qMin, self.head.index)
            # print(self.head.elem,'111')
            return
        else:
            # print(self.qMin, self.head.index)
            # print(self.head.next)
            self.head = self.head.next
            self.head.pre = None
            # print(self.head.elem,'222')

# print('x' * 50)
# text = Window([4, 3, 5, 4, 3, 3, 6, 7], 3, 5)
# text.makeWindow()
# print(text.head.elem)
# print(text.head.next.elem)
# print(text.head.next.index)
# print(text.head.next.next.elem)
# print(text.getMax().elem)
# print(text.head.next.pre.elem)
# print(text.head.next.next.elem)
# print(text.head.next.next.next.elem)
# print(text.head.next.next.next.next.elem)
print('x' * 50)


"""
生成窗口最大值数组：
有一个整形数组arr和一个大小为w的窗口从数组的左边滑到数组的右边，窗口每次向右滑动一个位置。
例如数组[4,3,5,4,3,3,6,7]，窗口大小为3时：
[4,3,5],4,3,3,6,7   窗口中最大值为5
4,[3,5,4],3,3,6,7   窗口中最大值为5
4,3,[5,4,3],3,6,7   窗口中最大值为5
4,3,5,[4,3,3],6,7   窗口中最大值为4
4,3,5,4,[3,3,6],7   窗口中最大值为6
4,3,5,4,3,[3,6,7]   窗口中最大值为7
如果数组长度为n 窗口大小为w 则一共产生n-w+1个窗口最大值
请实现一个函数 
输入整形数组arr 窗口大小w 
输出一个长度为n-w+1的数组res 表示每一个状态下的窗口最大值
如上面的例子应该返回 [5,5,5,4,6,7] 
"""


def getMaxArr(arr, w):
    helpArr = []
    length = len(arr)
    window = Window(arr, 0, w - 1)
    helpArr.append(window.getMax().elem)
    for _ in range(length - w):
        # print('text')
        window.extendWindow()
        window.reduceWindow()
        # print(window.head.elem)
        helpArr.append(window.getMax().elem)
    return helpArr


res = getMaxArr([4, 3, 5, 4, 3, 3, 6, 7], 3)
print(res)


# class Node(object):
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#         self.pre = None


# class Window(object):
#     def __init__(self, arr, qMin, qMax):
#         self.arr = arr
#         self.qMin = qMin
#         self.qMax = qMax
#         self.index = qMin
#         self.headNode = None
#         self._makeWindow()
#
#     def _makeWindow(self):
#         self.headNode = Node(self.index)
#         curNode = self.headNode
#         self.index += 1
#         while self.index <= self.qMax:
#             print('test')
#             while curNode.pre is not None:
#                 print(curNode.elem, curNode.pre.elem)
#                 if self.arr[curNode.elem] > self.arr[curNode.pre.elem]:
#                     print('test333')
#                     if curNode.pre.pre is None:
#                         self.headNode = curNode
#                         break
#                     curNode.pre = curNode.pre.pre
#                     curNode.pre.next = curNode
#                     curNode = curNode.pre
#                 else:
#                     break
#             newNode = Node(self.index)
#             curNode.next = newNode
#             newNode.pre = curNode
#             curNode = newNode
#             self.index += 1
#         return self.headNode
#
#     def expendWindow(self, new_qMax):
#         pass
#
#
# test = Window([1, 2, 3, 4, 5, 6, 7, 8], 1, 4)
# print(test.headNode.elem)
# print(test.index)
