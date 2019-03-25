# 一块金条切成两半，是需要花费和长度数值一样的铜板的。比如
# 长度为20的 金条，不管切成长度多大的两半，都要花费20个铜
# 板。一群人想整分整块金 条，怎么分最省铜板？
# 例如,给定数组{10,20,30}，代表一共三个人，整块金条长度为
# 10+20+30=60. 金条要分成10,20,30三个部分。 如果， 先把长
# 度60的金条分成10和50，花费60 再把长度50的金条分成20和30，
# 花费50 一共花费110铜板。
# 但是如果， 先把长度60的金条分成30和30，花费60 再把长度30
# 金条分成10和20，花费30 一共花费90铜板。
# 输入一个数组，返回分割的最小代价。


"""
思路(哈夫曼思想)：
（1）首先构造小根堆
（2）每次取最小的两个数（小根堆），使其代价最小。并将其和加入到小根堆中
（3）重复（2）过程，直到最后堆中只剩下一个节点。
注意：代价不是最后一个值，而是所有非叶节点之和，即上面求得两两节点之和。
"""
from extra.rootTree import SmallRootTree


class CutGolden(object):
    def __init__(self, arr):
        self.arr = arr
        self.smallRootTree = SmallRootTree(self.arr)

    def lessMoney(self):
        length = len(self.arr)
        # print(length)
        count = 0
        while length > 1:
            # print('test')
            length = len(self.arr)
            sum1 = self.arr.pop(0)
            length -= 1
            self.smallRootTree.heapInsert(length - 1)
            sum2 = self.arr.pop(0)
            count += sum1
            count += sum2
            self.arr.append(sum1 + sum2)
            self.smallRootTree.heapInsert(length - 1)
        return count


test = CutGolden([1, 3, 6, 6, 9, 16])
res = test.lessMoney()
print(res)
