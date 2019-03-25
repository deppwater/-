# 实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
# 【要求】
# 1．pop、push、getMin操作的时间复杂度都是O(1)。
# 2．设计的栈类型可以使用现成的栈结构。

"""
思路：
构造两个栈data和min
当添加数的时候分别添加进data与min
加入data的时候正常添加 加入min的时候需要判断要添加的数与min栈栈顶的数的大小
如果要添加的数小则在压入data的同时也压入min 反之min压一次自己的栈顶的数
当取出数的时候同时取出data栈和min栈的栈顶
"""


class Stack(object):
    def __init__(self, length):
        self.length = length
        self.index = 0
        self.queue_list = list()
        self.min_list = ['']

    def addNum(self, new_num):
        if self.min_list == ['']:
            self.min_list.append(new_num)
        elif new_num < self.min_list[-1]:
            self.min_list.append(new_num)
        else:
            self.min_list.append(self.min_list[-1])
        if self.index >= self.length:
            ex = Exception('队列已满')
            raise ex
        elif self.index < self.length:
            self.queue_list.append(new_num)
            self.index += 1
            print('添加成功')
            print(self.queue_list)

    def popNum(self):
        if self.index > 0:
            peek_num = self.queue_list[self.index - 1]
            self.queue_list.remove(peek_num)
            self.min_list.pop(-1)
            self.index -= 1
            print(peek_num)
        elif self.index == 0:
            ex = Exception('队列为空')
            raise ex

    def getMin(self):
        min_num = self.min_list[-1]
        return min_num


# stack = Stack(9)
# stack.addNum(13)
# stack.addNum(9)
# stack.addNum(11)
# stack.addNum(7)
# stack.addNum(5)
# stack.addNum(3)
# stack.popNum()
# stack.popNum()
# stack.popNum()
# stack.popNum()
# print('=' * 50)
# result = stack.getMin()
# print(result)


# 方法二
class TwoStack(object):
    def __init__(self):
        self.index = 0
        self.data = []
        self.min = []

    def push(self, num):
        self.data.append(num)
        self.min.append(num if not self.min else min(self.min[self.index - 1], num))
        self.index += 1

    def pop(self):
        if not self.data:
            ex = Exception('栈为空')
            raise ex
        print(self.data.pop(self.index - 1))
        self.min.pop(self.index - 1)
        self.index -= 1

    def getMin(self):
        print(self.min[self.index - 1])


q = TwoStack()
q.push(2)
q.push(5)
q.push(3)
q.push(4)
q.push(1)
q.pop()
q.pop()
q.pop()
q.getMin()
q.getMin()
q.getMin()