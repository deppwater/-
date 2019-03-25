"""
思路：
准备两个队列data和help
当添加数的时候 数直接进入队列data
当取出数的时候 先把队列data长度减1的数取出并加入help队列
然后交换data与help的引用 弹出help队列中的数 此时help队列中只剩下原来data队列最后加入的数
"""

import queue


class BeingStark(object):
    def __init__(self):
        self.data = queue.Queue()
        self.help = queue.Queue()

    def addNum(self, new_num):
        self.data.put(new_num)
        return self.data

    def getNum(self):
        if self.data:
            for i in range(self.data.qsize() - 1):
                self.help.put(self.data.get())
        self.data, self.help = self.help, self.data
        return self.help.get()


text_queue = BeingStark()
text_queue.addNum(1)
text_queue.addNum(2)
text_queue.addNum(3)
text_queue.addNum(4)
text_queue.addNum(5)
result = text_queue.getNum()
print(result)
result1 = text_queue.getNum()
print(result1)
result2 = text_queue.getNum()
print(result2)