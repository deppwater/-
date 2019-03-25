"""
思路：
准备两个栈push和pop
新来的数永远加入push栈
当要取数的时候 先判断pop栈是否为空
如果pop栈不为空 直接弹出pop栈的栈顶
如果pop栈为空 直接将push栈的数弹出并加入pop栈且要一次加完
然后判断此时的pop栈是否为空 如果不为空 弹出pop栈栈顶
如果为空 则返回队列为空
"""

import queue


class BeingQueue(object):
    def __init__(self):
        self.push = queue.LifoQueue()
        self.pop = queue.LifoQueue()

    def addNum(self, new_num):
        self.push.put(new_num)

    def getNum(self):
        if self.pop.empty():
            while self.push.qsize() > 0:
                self.pop.put(self.push.get())
        if not self.pop.empty():
            return self.pop.get()
        elif self.pop.empty():
            return '队列为空'


stark = BeingQueue()
stark.addNum(1)
result = stark.getNum()
print(result)
stark.addNum(2)
stark.addNum(3)
stark.addNum(4)
stark.addNum(5)

result = stark.getNum()
print(result)
result = stark.getNum()
print(result)
result = stark.getNum()
print(result)
result = stark.getNum()
print(result)
result = stark.getNum()
print(result)
