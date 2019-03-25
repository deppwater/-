# help_set = set()
# help_count = 0
#
#
# def pNum(max_num):
#     for i in range(2, max_num // 2):
#         help_set.add(i * 2)
#     print(max_num - len(help_set))
#
#
# pNum(100)
# for j in range(4, 0, -1):
#     print(j)
#
# string = 'abcd'
#
# aa = '#'.join('#' + string + '#')
# print(aa)
#
# a = [1]
# b = 1
# while b == 1:
#     b = a.pop()
# print(b)

# print(-1 >> 1)
#
# print(2 << 1 + 1)
# print((2 << 1) + 1)

# arr = [1, 3, 5, 7, 6, 4, 2]
# print(arr.sort())
# print(arr)

# 在一大堆数中求出其前k大或前k小的所有数，简称TOP-K问题。目前解决TOP-K问题最有效的算法即是BFPRT算法，又称为中位数的中位数算法，
# 该算法由Blum、Floyd、Pratt、Rivest、Tarjan提出，最坏时间复杂度为O(n)。
#
# 首次遇到接触TOP-K问题时，第一反应是可以先对所有数据进行一次排序，然后取其前k即可，但是这么做有两个问题：
# （1）：快速排序的平均复杂度为，但最坏时间复杂度为，不能始终保证较好的复杂度。
# （2）：我们只需要前k大的，而对其余不需要的数也进行了排序，浪费了大量排序时间。
#
# 除上述方法外，堆排序也是一个比较好的选择，可以维护一个大小为k的堆，时间复杂度为O(nlogk)。

"""
一个相对优良的算法：
利用快速排序优化版 即用荷兰国旗问题优化后的快速排序
即将数组分为三个区域 大于等于小于区域 区别在于用等于区域的范围跟TOP-K的范围进行比较
如果TOP-K小于等于区域的左边界 左半边继续排序 而右半边则不需要排序
这样达到的效果是最坏时间复杂度为O(N^2) 最优时间复杂度为O(N) 基于概率的数学期望为O(N)

快速排序的过程，以升序为例：
（1）：选取基准元素（首元素，尾元素或一个随机元素）；
（2）：以选取的基准元素为分界点，把小于基准元素的放在左边，大于基准元素的放在右边；
（3）：分别对左边和右边进行递归，重复上述过程。

BFPRT算法：
在选取哪个数作为等于区域的划分值的时候进行了优化 时间复杂度不基于概率 严格的O(N)
步骤：
（1）：将数组分为接近N/5组 每组5个数 最后一组不满5个数单独分为一组
（2）：每个组内之间进行排序 5个数之间排序 时间复杂度为O(1) 那么有N/5组 时间复杂度为O(N)
（3）：将每组的中位数拿出来组成新的数组 如果数量为偶数那么规定好取上中位数或下中位数 组成一个长度为N/5长度的数组
（4）：递归调用BFPRT算法求中位数中的中位数 即求出整个数组的中位数n 即：BFPRT(new_arr, len(new_arr)/2 + 1)
      如果被划分的new_arr小于5了 那么可以直接得到中位数
（5）：以n为划分值进行一组快速排序优化版 判断基准元素位置i与k的大小
      如果i==k，返回x
      如果i<k，在小于x的元素中递归查找第i小的元素
      如果i>k，在大于等于x的元素中递归查找第i-k小的元素
（6）：时间复杂度：
      当确定n之后可以确定最多有7N/10个数比n要小 也最多有7N/10个数比n要大
      所以时间复杂度计算公式为：T(N) = T(N/5) + T(7N/10) + O(N) = O(N)
"""

"""
堆排解法

用堆排来解决Top K的思路很直接。堆排利用的大（小）顶堆所有子节点元素都比父节点小（大）的性质来实现的，
既然一个大顶堆的顶是最大的元素，那我们要找最小的K个元素，是不是可以先建立一个包含K个元素的堆，
然后遍历集合，如果集合的元素比堆顶元素小（说明它目前应该在K个最小之列），那就用该元素来替换堆顶元素，
同时维护该堆的性质，那在遍历结束的时候，堆中包含的K个元素是不是就是我们要找的最小的K个元素？ 

速记口诀：最小的K个用最大堆，最大的K个用最小堆。

时间复杂度：O(n*logK)
适用场景：实现的过程中，先用前K个数建立了一个堆，然后遍历数组来维护这个堆。这种做法带来了三个好处：
（1）不会改变数据的输入顺序（按顺序读的）；
（2）不会占用太多的内存空间（事实上，一次只读入一个数，内存只要求能容纳前K个数即可）；
（3）由于（2），决定了它特别适合处理海量数据。

此处先假设求前K小的数 前K大的数过程类似
"""


class HeapTopK(object):
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        self.helpArr = arr[k:]

    def heapSort(self):
        if len(self.arr) < 2:
            return self.arr

        for i in range(self.k):
            self.heapInsert(i)
        # print(self.arr)
        # print(self.arr)
        # print(self.helpArr)
        for j in self.helpArr:
            if j <= self.arr[0]:
                self.arr[0], j = j, self.arr[0]
                self.heapify(0)
            # print(self.arr)
        return self.arr[:self.k]

    def heapInsert(self, index):
        # 如果不好想范围 可以考虑最极端的情况
        while self.arr[index] > self.arr[(index - 1) >> 1]:
            if (index - 1) >> 1 == -1:
                break
            self.arr[index], self.arr[(index - 1) >> 1] = self.arr[(index - 1) >> 1], self.arr[index]
            index = (index - 1) >> 1

    def heapify(self, index):
        left = (index << 1) + 1
        while left < self.k:
            # 这个largest为两个子孩子中较大的
            # 这里要加上=是因为数组里会出现相同的数的情况
            largest = left if left + 1 < self.k and self.arr[left] > self.arr[left + 1] else left + 1
            # 此时largest为两个子孩子中较大的与当前index中较大的
            largest = largest if self.arr[largest] > self.arr[index] else index
            if largest == index:
                break
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            index = largest
            left = (index << 1) + 1


# test = HeapTopK([7, 5, 7, 4, 4, 4, 4, 2], 5)
# res = test.heapSort()
# print(res)

"""
快排解法

用快排的思想来解Top K问题，必然要运用到”分治”。

与快排相比，两者唯一的不同是在对”分治”结果的使用上。
我们知道，分治函数会返回一个position，在position左边的数都比第position个数小，
在position右边的数都比第position大。我们不妨不断调用分治函数，
直到它输出的position = K-1，此时position前面的K个数（0到K-1）就是要找的前K个数。

时间复杂度：O(n)

适用场景：对照着堆排的解法来看，partition函数会不断地交换元素的位置，
所以它肯定会改变数据输入的顺序；既然要交换元素的位置，那么所有元素必须要读到内存空间中，
所以它会占用比较大的空间，至少能容纳整个数组；数据越多，占用的空间必然越大，海量数据处理起来相对吃力。

但是，它的时间复杂度很低，意味着数据量不大时，效率极高。

此处求前k小的数 求前k大的数只需改变判断条件即可
"""
import random


class QuickSortTopK(object):
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k - 1
        self.low = 0
        self.high = len(self.arr) - 1

    def getMinKNumsByQuick(self):
        if self.arr is None or len(self.arr) < 1 or len(self.arr) < self.k:
            return -1
        index = self.partition()
        while self.k < index[0] or self.k > index[1]:
            if index[1] < self.k:
                self.low = index[1] + 1
                # 这里不给index重新赋值 index依然是第一次的结果
                index = self.partition()

            if index[0] > self.k:
                self.high = index[0] - 1
                index = self.partition()

        return self.arr[:self.k + 1]

    def partition(self):
        mid = random.randint(self.low, self.high)
        base_num = self.arr[mid]
        less = self.low - 1
        more = self.high + 1
        cur = self.low
        # print('test')
        while cur < more:
            if self.arr[cur] < base_num:
                self.arr[less + 1], self.arr[cur] = self.arr[cur], self.arr[less + 1]
                cur += 1
                less += 1
            elif self.arr[cur] == base_num:
                cur += 1
            else:
                self.arr[more - 1], self.arr[cur] = self.arr[cur], self.arr[more - 1]
                more -= 1
        # print([less + 1, more - 1])
        # print(self.arr)
        return [less + 1, more - 1]


# test = QuickSortTopK([7, 5, 7, 4, 4, 4, 4, 2], 4)
# res = test.getMinKNumsByQuick()
# print(res)


class BFPRT(object):
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k - 1
        self.low = 0
        self.high = len(self.arr) - 1
        helpArr = self.arr
        print(self.splitArr(helpArr))

    # def do(self):
    #     helpArr = self.arr
    #     self.splitArr(helpArr)
        # if res is not None:
        #     return res

    def splitArr(self, helpArr):
        # if len(helpArr) == 1:
        #     print(self.arr[:self.k + 1])
        #     return
        parts = len(helpArr) // 5 if len(helpArr) % 5 == 0 else len(helpArr) // 5 + 1
        newArr = [['']] * parts
        for i in range(parts):
            newArr[i] = helpArr[i * 5:i * 5 + 5]
        return self.findMedian(newArr, parts)
        # if res is not None:
        #     return res

    def findMedian(self, arr, parts):
        helpArr = []
        # print(arr, parts)
        for i in range(parts):
            newArr = self.insertSort(arr[i])
            helpArr.append(newArr[len(arr[i]) // 2])
        # print(helpArr)
        if len(helpArr) == 1:
            return self.partition(helpArr[0])
            # if res is not None:
            #     return res
        return self.splitArr(helpArr)
        # if res is not None:
        #     return res

    @staticmethod
    def insertSort(arr):
        index = 1
        while index < len(arr):
            helpIndex = index
            while arr[helpIndex] < arr[helpIndex - 1] and helpIndex > 0:
                arr[helpIndex], arr[helpIndex - 1] = arr[helpIndex - 1], arr[helpIndex]
                helpIndex -= 1
            index += 1
        return arr

    def partition(self, baseNum):
        # print('test')
        # print(self.low, self.high)
        less = self.low - 1
        more = self.high + 1
        cur = self.low
        while cur < more:
            if self.arr[cur] < baseNum:
                self.arr[less + 1], self.arr[cur] = self.arr[cur], self.arr[less + 1]
                cur += 1
                less += 1
            elif self.arr[cur] == baseNum:
                cur += 1
            else:
                self.arr[more - 1], self.arr[cur] = self.arr[cur], self.arr[more - 1]
                more -= 1
        # print((less + 1, more))
        if self.k in range(less + 1, more):
            return self.arr[:self.k + 1]
        elif self.k < less + 1:
            self.high = less
            return self.splitArr(self.arr[self.low:self.high + 1])
            # if res is not None:
            #     return res
        else:
            self.low = more
            return self.splitArr(self.arr[self.low:self.high + 1])
            # if res is not None:
            #     return res

import time


time1 = time.time()
# BFPRT 4.90710186958313
# QuickSortTopK 2.004970073699951
# HeapTopK 3.1659910678863525
for topK in range(1, 22):
    test = HeapTopK([8, 13, 5, 7, 17, 3, 12, 6, 6, 6, 2, 6, 6, 21, 16, 4, 20, 11, 15, 10, 1, 22], topK)
    # print(res)
    test.heapSort()
time2 = time.time()
print(time2 - time1)


# test = BFPRT([8, 13, 5, 7, 17, 3, 12, 6, 6, 6, 2, 6, 6, 21, 16, 4, 20, 11, 15, 10, 1, 22], 20)
# print(test.arr)
# res = test.do()
# print(res)
# print(test)
# print(test.arr)
# helpArr = [8, 13, 5, 7, 17, 3, 12, 6, 19, 9, 2, 14, 18, 21, 16, 4, 20, 11, 15, 10, 1, 22]

