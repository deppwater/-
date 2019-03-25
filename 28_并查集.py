"""
概念：
给定两个集合set1和set2 以及两个元素A和B 其中的元素已事先给定
要求快速的查询出A和B是否在同一集合 以及假设A属于set1 B属于set2
要求快速的合并A所在的set1和B所在的set2

思路：
先确定集合中的数据结构 首先假设每个元素所在的集合只有自己 且自己为自己所在集合的代表节点(头结点)
每个节点有一个指向自己的指针
然后在这个几个元素中选定一个代表节点 让其他所有节点原本指向自己的指针挨个串起来
可以有多条串同时挂在一个代表节点上 即多叉树
这样isSameSet的过程就是两个元素各自往上查找自己集合的代表节点的过程
union过程就是让元素数量更少的集合挂在元素更多集合下面的过程

优化思路：
在每一次向上查找代表节点的过程中(可能是isSameSet也可能是union) 将该节点过程中路过的所有节点都直接挂在代表节点上
而该节点本身也直接挂在代表节点上 但该节点后面挂着的数保持不变

时间复杂度：
当有N个数据样本 且查询次数+合并次数逼近了O(N)及以上
那么单次操作不管查询还是合并的复杂度都是O(1)
"""


class UnionFindSet(object):
    def __init__(self, *args):
        self.node_li = args
        # 对应关系为{子节点:父节点}
        # print(self.node_li)
        self.fatherMap = {}
        self.sizeMap = {}
        for node in self.node_li:
            self.fatherMap[node] = node
            self.sizeMap[node] = 1

    def findHead(self, node):
        father_node = self.fatherMap[node]
        if father_node != node:
            self.findHead(father_node)
        self.fatherMap[node] = father_node
        return father_node

    def isSameSet(self, nodeA, nodeB):
        return self.findHead(nodeA) == self.findHead(nodeB)

    def union(self, nodeA, nodeB):
        if nodeA is None or nodeB is None:
            return
        aHead = self.findHead(nodeA)
        bHead = self.findHead(nodeB)
        if aHead != bHead:
            aSetSize = self.sizeMap[aHead]
            bSetSize = self.sizeMap[bHead]
            if aSetSize <= bSetSize:
                self.fatherMap[aHead] = bHead
                self.sizeMap[bHead] = aSetSize + bSetSize
            else:
                self.fatherMap[bHead] = aHead
                self.sizeMap[aHead] = aSetSize + bSetSize


if __name__ == '__main__':
    text = UnionFindSet(1, 2, 3, 4, 5, 6)

    # res = text.isSameSet(1, 2)
    text.union(1, 2)
    res = text.findHead(1)
    print(res)

