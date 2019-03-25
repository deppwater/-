"""
思路：
设置一个index指针 建立一个数组A长度为length 那么此时index指向数组A的0位置
当添加数字进去的时候 数字添加到index指向的位置 index+=1
当取数字的时候 从index-1位置取数字 index-=1
判断当index>length的时候不能再添加数字
"""


class Stack(object):
    def __init__(self, length):
        self.length = length
        self.index = 0
        self.queue_list = list()

    def addNum(self, new_num):
        if self.index >= self.length:
            ex = Exception('队列已满')
            raise ex
        elif self.index < self.length:
            self.queue_list += ['']
            self.queue_list[self.index] = new_num
            self.index += 1
            print('添加成功')
            print(self.queue_list)

    def popNum(self):
        if self.index > 0:
            peek_num = self.queue_list[self.index - 1]
            self.index -= 1
            self.queue_list[self.index] = ''
            print(peek_num)
        elif self.index == 0:
            ex = Exception('队列为空')
            raise ex


queue = Stack(6)
queue.addNum(5)
queue.addNum(4)
queue.addNum(3)
queue.addNum(2)
queue.addNum(1)
queue.addNum(0)
# queue.addNum(6)
# queue.addNum(7)
# queue.addNum(8)
queue.popNum()
queue.popNum()
queue.popNum()
queue.popNum()
queue.popNum()
queue.popNum()
# queue.popNum()
# queue.popNum()
