
"""
思路：
设置两个指针start和end 假设队列总长度为length 用size来记录当前队列的尺寸
start与end初始都在数组的0位置 此时size等于0 length为可自定义的
当添加一个数的时候 添加到end所指的位置 end+1 size+1 当end大于length的时候 end=0 且size不能大于length
当取出一个数的时候 取出start所指的位置 start+1 size-1 当start大于length的时候 start=0 且size必须大于0
"""


class Queue(object):
    def __init__(self, length):
        self.length = length
        self.start = 0
        self.end = 0
        self.size = 0
        self.first_num = 0
        self.num_list = [[]] * self.length

    def addNum(self, new_num):
        # print(self.end)
        print(self.num_list[self.end])
        if self.size < self.length:
            self.num_list[self.end] = new_num
            self.size += 1
            if self.end != self.length - 1:
                self.end += 1
            else:
                self.end = 0
            print('添加成功')
            print(self.num_list)
        else:
            ex = Exception('队列已满')
            raise ex

    def popNum(self):
        if self.size > 0:
            self.first_num = self.num_list[self.start]
            self.num_list[self.start] = []
            self.size -= 1
            if self.first_num is []:
                ex = Exception('队列为空')
                raise ex

            # self.size -= 1
            print(self.first_num)
            if self.start != self.length - 1:
                self.start += 1
            else:
                self.start = 0


# queue = Queue(5)
# queue.addNum(5)
# queue.popNum()
# queue.addNum(4)
# queue.addNum(3)
# queue.addNum(2)
# queue.addNum(1)
# # queue.addNum(0)
# queue.popNum()
# queue.popNum()
# queue.popNum()
# queue.addNum(9)
# queue.addNum(8)
# queue.addNum(7)
# queue.popNum()
# queue.popNum()
# queue.popNum()
# queue.addNum(6)
# queue.popNum()
# queue.popNum()
# queue.popNum()
# queue.popNum()


# 方法二
class ArrayQueue(object):
    def __init__(self, length):
        self.length = length
        self.size = 0
        self.start = 0
        self.end = 0
        self.queue = [[]] * length

    def add(self, num):
        if self.size == self.length:
            ex = Exception('队列已满')
            raise ex
        self.queue[self.end] = num
        self.end = self.end + 1 if self.end < self.length - 1 else 0
        self.size += 1

    def pop(self):
        if self.size == 0:
            ex = Exception('队列为空')
            raise ex
        print(self.queue[self.start])
        self.start = self.start + 1 if self.start < self.length - 1 else 0
        self.size -= 1


q = ArrayQueue(5)
q.add(1)
q.pop()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)
q.add(5)
q.add(2)
q.pop()
q.pop()
q.pop()
q.pop()
q.pop()
