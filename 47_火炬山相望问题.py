"""
题目：
给定一个列表 表示一个首尾相连的高度为列表中元素的山峰
规则：
1.如果两个山峰相邻 那么两个山峰为一对可见山峰
2.如果两个山峰之间没有比两个山峰较低的山峰高的山峰 那么这两个山峰为一对可见山峰
问：
一共有多少对可见山峰
"""

"""
如果山峰的高度都不相同 有结论：
当山峰个数为0和1的时候 可见山峰对为0
当山峰个数为2的时候 可见山峰对为1
当山峰个数超过2的时候 可见山峰对为（n*2-3）
证明：
取这个山峰最高点和次高点 
那么这两点之间的任意一个山峰向两边找 找到离得最近的最大的停止
一定可以凑成一对 如果再继续找找到的这个山峰一定会挡住原山峰 且最多只能找到最高的或者次高的山峰
此时可见山峰对一共有（n-2）*2即 2n-4对
再加上最高的和次高的成一对 那么一共有2n-3对
"""

"""
如果存在相同高度的山峰 则需要利用单调栈：
找到山峰中最高的山峰 如果有多个相同的最高的 则只找第一个
从这个山峰开始遍历整个山峰
需要用到的单调栈结构为从底部到顶部为由大到小 节点记录的数据为遍历到的山峰高度和相同高度的山峰个数
弹出条件为新加入的山峰高度大于栈顶山峰的高度
结算这个被弹出的山峰的可见山峰对规则为：
1.如果相同高度的只有一个 那么可见山峰对为2
2.如果相同高度的大于一个 那么可见山峰对为Cn2(n为底 为相同高度的山峰个数)+2*n
注意：
以最大值作为起始的原因是接下来的数按正确方向一定能找到比它大的数
最后上述逻辑完成后还需要进行结算 此时的结算较为特殊：
1.当栈里还有两个以上的节点的时候 依然按照上述第二种情况结算
2.栈里倒数第二个数进行结算 如果栈底的那个数有2个或者2个以上 依然按照上述第二种情况进行结算
  但栈底的那个数只有1个 则结果变为Cn2+1*n
3.栈里最后一个数进行结算 如果只有1个 那么为0 如果有2个或者2个以上 则为Cn2
"""

from queue import LifoQueue


class Node(object):
    def __init__(self, high, count=1):
        self.high = high
        self.count = count


class Communications(object):
    def __init__(self, arr):
        self.arr = arr
        # 构造一个底部到顶部为从大到小的栈
        self.helpQueue = LifoQueue()
        self.findBeginning()
        self.length = len(self.arr)
        self.count = 0

    def findBeginning(self):
        # 找到第一个最大的数并作为数组第一个数
        maximum = max(self.arr)
        maxIndex = self.arr.index(maximum)
        arrA = self.arr[:maxIndex]
        arrB = self.arr[maxIndex:]
        self.arr = arrB + arrA

    def communicate(self):
        helpIndex = 0
        newNode = Node(self.arr[helpIndex])
        self.helpQueue.put(newNode)
        helpIndex += 1
        while helpIndex <= self.length - 1:
            # 拿取当前栈顶的节点数据
            curNode = self.helpQueue.get()
            self.helpQueue.put(curNode)
            # 建立新的节点
            newNode = Node(self.arr[helpIndex])
            # 因为起始的数为当前列表的最大值 因此在这个过程中栈不可能空 可以去掉 and not self.helpQueue.empty() 的判断
            while curNode.high < newNode.high:
                alreadyOutNode = self.helpQueue.get()
                if alreadyOutNode.count == 1:
                    self.count += 2
                else:
                    self.count += alreadyOutNode.count * (alreadyOutNode.count - 1) / 2 + 2 * alreadyOutNode.count
                curNode = self.helpQueue.get()
                # 这是只是需要拿出节点数据 因此还需要再放回去
                self.helpQueue.put(curNode)
            if newNode.high == curNode.high:
                curNode = self.helpQueue.get()
                curNode.count += 1
                self.helpQueue.put(curNode)
            else:
                self.helpQueue.put(newNode)
            helpIndex += 1

        # 接下来进行最后剩余的结算
        # print('test')
        # print(self.helpQueue.qsize())
        # print(self.count)
        while not self.helpQueue.empty():
            helpSize = self.helpQueue.qsize()
            while helpSize > 2:
                curNode = self.helpQueue.get()
                self.count += curNode.count * (curNode.count - 1) / 2 + 2 * curNode.count
                helpSize = self.helpQueue.qsize()
            if helpSize == 2:
                curNode = self.helpQueue.get()
                lastNode = self.helpQueue.get()
                self.helpQueue.put(lastNode)
                if lastNode.count == 1:
                    # 此处就是数学问题了 可以不分成两种情况 因为c12按公式算出的结果就是0
                    if curNode.count > 1:
                        self.count += curNode.count * (curNode.count - 1) / 2 + 1 * curNode.count
                    else:
                        self.count += 1
                else:
                    self.count += curNode.count * (curNode.count - 1) / 2 + 2 * curNode.count
            if helpSize == 1:
                curNode = self.helpQueue.get()
                if curNode.count > 1:
                    self.count += curNode.count * (curNode.count - 1) / 2

        return int(self.count)


arr = [4, 3, 2, 5, 5, 7, 5, 6]
test = Communications(arr)
print(test.arr)
res = test.communicate()
print(res)
