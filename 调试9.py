# # help_set = set()
# # help_count = 0
# #
# #
# # def pNum(max_num):
# #     for i in range(2, max_num // 2):
# #         help_set.add(i * 2)
# #     print(max_num - len(help_set))
# #
# #
# # pNum(100)
# # for j in range(4, 0, -1):
# #     print(j)
# #
# # string = 'abcd'
# #
# # aa = '#'.join('#' + string + '#')
# # print(aa)
# #
# # a = [1]
# # b = 1
# # while b == 1:
# #     b = a.pop()
# # print(b)
#
# # print(-1 >> 1)
# #
# # print(2 << 1 + 1)
# # print((2 << 1) + 1)
#
# # arr = [1, 3, 5, 7, 6, 4, 2]
# # print(arr.sort())
# # print(arr)
#
# # 在一大堆数中求出其前k大或前k小的所有数，简称TOP-K问题。目前解决TOP-K问题最有效的算法即是BFPRT算法，又称为中位数的中位数算法，
# # 该算法由Blum、Floyd、Pratt、Rivest、Tarjan提出，最坏时间复杂度为O(n)。
# #
# # 首次遇到接触TOP-K问题时，第一反应是可以先对所有数据进行一次排序，然后取其前k即可，但是这么做有两个问题：
# # （1）：快速排序的平均复杂度为，但最坏时间复杂度为，不能始终保证较好的复杂度。
# # （2）：我们只需要前k大的，而对其余不需要的数也进行了排序，浪费了大量排序时间。
# #
# # 除上述方法外，堆排序也是一个比较好的选择，可以维护一个大小为k的堆，时间复杂度为O(nlogk)。
#
# # """
# # 一个相对优良的算法：
# # 利用快速排序优化版 即用荷兰国旗问题优化后的快速排序
# # 即将数组分为三个区域 大于等于小于区域 区别在于用等于区域的范围跟TOP-K的范围进行比较
# # 如果TOP-K小于等于区域的左边界 左半边继续排序 而右半边则不需要排序
# # 这样达到的效果是最坏时间复杂度为O(N^2) 最优时间复杂度为O(N) 基于概率的数学期望为O(N)
# #
# # 快速排序的过程，以升序为例：
# # （1）：选取基准元素（首元素，尾元素或一个随机元素）；
# # （2）：以选取的基准元素为分界点，把小于基准元素的放在左边，大于基准元素的放在右边；
# # （3）：分别对左边和右边进行递归，重复上述过程。
# #
# # BFPRT算法：
# # 在选取哪个数作为等于区域的划分值的时候进行了优化 时间复杂度不基于概率 严格的O(N)
# # 步骤：
# # （1）：将数组分为接近N/5组 每组5个数 最后一组不满5个数单独分为一组
# # （2）：每个组内之间进行排序 5个数之间排序 时间复杂度为O(1) 那么有N/5组 时间复杂度为O(N)
# # （3）：将每组的中位数拿出来组成新的数组 如果数量为偶数那么规定好取上中位数或下中位数 组成一个长度为N/5长度的数组
# # （4）：递归调用BFPRT算法求中位数中的中位数 即求出整个数组的中位数n 即：BFPRT(new_arr, len(new_arr)/2 + 1)
# #       如果被划分的new_arr小于5了 那么可以直接得到中位数
# # （5）：以n为划分值进行一组快速排序优化版 判断基准元素位置i与k的大小
# #       如果i==k，返回x
# #       如果i<k，在小于x的元素中递归查找第i小的元素
# #       如果i>k，在大于等于x的元素中递归查找第i-k小的元素
# # （6）：时间复杂度：
# #       当确定n之后可以确定最多有7N/10个数比n要小 也最多有7N/10个数比n要大
# #       所以时间复杂度计算公式为：T(N) = T(N/5) + T(7N/10) + O(N) = O(N)
# # """
# #
# # """
# # 堆排解法
# #
# # 用堆排来解决Top K的思路很直接。堆排利用的大（小）顶堆所有子节点元素都比父节点小（大）的性质来实现的，
# # 既然一个大顶堆的顶是最大的元素，那我们要找最小的K个元素，是不是可以先建立一个包含K个元素的堆，
# # 然后遍历集合，如果集合的元素比堆顶元素小（说明它目前应该在K个最小之列），那就用该元素来替换堆顶元素，
# # 同时维护该堆的性质，那在遍历结束的时候，堆中包含的K个元素是不是就是我们要找的最小的K个元素？ 
# #
# # 速记口诀：最小的K个用最大堆，最大的K个用最小堆。
# #
# # 时间复杂度：O(n*logK)
# # 适用场景：实现的过程中，先用前K个数建立了一个堆，然后遍历数组来维护这个堆。这种做法带来了三个好处：
# # （1）不会改变数据的输入顺序（按顺序读的）；
# # （2）不会占用太多的内存空间（事实上，一次只读入一个数，内存只要求能容纳前K个数即可）；
# # （3）由于（2），决定了它特别适合处理海量数据。
# #
# # 此处先假设求前K小的数 前K大的数过程类似
# # """
# #
# #
# # class HeapTopK(object):
# #     def __init__(self, arr, k):
# #         self.arr = arr
# #         self.k = k
# #         self.helpArr = arr[k:]
# #
# #     def heapSort(self):
# #         if len(self.arr) < 2:
# #             return self.arr
# #
# #         for i in range(self.k):
# #             self.heapInsert(i)
# #         print(self.arr)
# #         # print(self.arr)
# #         # print(self.helpArr)
# #         for j in self.helpArr:
# #             if j <= self.arr[0]:
# #                 self.arr[0], j = j, self.arr[0]
# #                 self.heapify(0)
# #             print(self.arr)
# #         return self.arr[:self.k]
# #
# #     def heapInsert(self, index):
# #         # 如果不好想范围 可以考虑最极端的情况
# #         while self.arr[index] > self.arr[(index - 1) >> 1]:
# #             if (index - 1) >> 1 == -1:
# #                 break
# #             self.arr[index], self.arr[(index - 1) >> 1] = self.arr[(index - 1) >> 1], self.arr[index]
# #             index = (index - 1) >> 1
# #
# #     def heapify(self, index):
# #         left = (index << 1) + 1
# #         while left < self.k:
# #             # 这个largest为两个子孩子中较大的
# #             # 这里要加上=是因为数组里会出现相同的数的情况
# #             largest = left if left + 1 < self.k and self.arr[left] > self.arr[left + 1] else left + 1
# #             # 此时largest为两个子孩子中较大的与当前index中较大的
# #             largest = largest if self.arr[largest] > self.arr[index] else index
# #             if largest == index:
# #                 break
# #             self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
# #             index = largest
# #             left = (index << 1) + 1
# #
# #
# # # test = HeapTopK([7, 5, 7, 4, 4, 4, 4, 2], 5)
# # # res = test.heapSort()
# # # print(res)
# #
# # """
# # 快排解法
# #
# # 用快排的思想来解Top K问题，必然要运用到”分治”。
# #
# # 与快排相比，两者唯一的不同是在对”分治”结果的使用上。
# # 我们知道，分治函数会返回一个position，在position左边的数都比第position个数小，
# # 在position右边的数都比第position大。我们不妨不断调用分治函数，
# # 直到它输出的position = K-1，此时position前面的K个数（0到K-1）就是要找的前K个数。
# #
# # 时间复杂度：O(n)
# #
# # 适用场景：对照着堆排的解法来看，partition函数会不断地交换元素的位置，
# # 所以它肯定会改变数据输入的顺序；既然要交换元素的位置，那么所有元素必须要读到内存空间中，
# # 所以它会占用比较大的空间，至少能容纳整个数组；数据越多，占用的空间必然越大，海量数据处理起来相对吃力。
# #
# # 但是，它的时间复杂度很低，意味着数据量不大时，效率极高。
# #
# # 此处求前k小的数 求前k大的数只需改变判断条件即可
# # """
# # import random
# #
# #
# # class QuickSortTopK(object):
# #     def __init__(self, arr, k):
# #         self.arr = arr
# #         self.k = k - 1
# #         self.low = 0
# #         self.high = len(self.arr) - 1
# #
# #     def getMinKNumsByQuick(self):
# #         if self.arr is None or len(self.arr) < 1 or len(self.arr) < self.k:
# #             return -1
# #         index = self.partition()
# #         while self.k < index[0] or self.k > index[1]:
# #             if index[1] < self.k:
# #                 self.low = index[1] + 1
# #                 # 这里不给index重新赋值 index依然是第一次的结果
# #                 index = self.partition()
# #
# #             if index[0] > self.k:
# #                 self.high = index[0] - 1
# #                 index = self.partition()
# #
# #         return self.arr[:self.k + 1]
# #
# #     def partition(self):
# #         mid = random.randint(self.low, self.high)
# #         base_num = self.arr[mid]
# #         less = self.low - 1
# #         more = self.high + 1
# #         cur = self.low
# #         print('test')
# #         while cur < more:
# #             if self.arr[cur] < base_num:
# #                 self.arr[less + 1], self.arr[cur] = self.arr[cur], self.arr[less + 1]
# #                 cur += 1
# #                 less += 1
# #             elif self.arr[cur] == base_num:
# #                 cur += 1
# #             else:
# #                 self.arr[more - 1], self.arr[cur] = self.arr[cur], self.arr[more - 1]
# #                 more -= 1
# #         # print([less + 1, more - 1])
# #         print(self.arr)
# #         return [less + 1, more - 1]
# #
# #
# # # test = QuickSortTopK([7, 5, 7, 4, 4, 4, 4, 2], 4)
# # # res = test.getMinKNumsByQuick()
# # # print(res)
# #
# #
# # class BFPRT(object):
# #     def __init__(self, arr, k):
# #         self.arr = arr
# #         self.k = k - 1
# #         self.low = 0
# #         self.high = len(self.arr) - 1
# #         helpArr = self.arr
# #         print(self.splitArr(helpArr))
# #
# #     # def do(self):
# #     #     helpArr = self.arr
# #     #     self.splitArr(helpArr)
# #         # if res is not None:
# #         #     return res
# #
# #     def splitArr(self, helpArr):
# #         # if len(helpArr) == 1:
# #         #     print(self.arr[:self.k + 1])
# #         #     return
# #         parts = len(helpArr) // 5 if len(helpArr) % 5 == 0 else len(helpArr) // 5 + 1
# #         newArr = [['']] * parts
# #         for i in range(parts):
# #             newArr[i] = helpArr[i * 5:i * 5 + 5]
# #         return self.findMedian(newArr, parts)
# #         # if res is not None:
# #         #     return res
# #
# #     def findMedian(self, arr, parts):
# #         helpArr = []
# #         # print(arr, parts)
# #         for i in range(parts):
# #             newArr = self.insertSort(arr[i])
# #             helpArr.append(newArr[len(arr[i]) // 2])
# #         # print(helpArr)
# #         if len(helpArr) == 1:
# #             return self.partition(helpArr[0])
# #             # if res is not None:
# #             #     return res
# #         return self.splitArr(helpArr)
# #         # if res is not None:
# #         #     return res
# #
# #     @staticmethod
# #     def insertSort(arr):
# #         index = 1
# #         while index < len(arr):
# #             helpIndex = index
# #             while arr[helpIndex] < arr[helpIndex - 1] and helpIndex > 0:
# #                 arr[helpIndex], arr[helpIndex - 1] = arr[helpIndex - 1], arr[helpIndex]
# #                 helpIndex -= 1
# #             index += 1
# #         return arr
# #
# #     def partition(self, baseNum):
# #         # print('test')
# #         # print(self.low, self.high)
# #         less = self.low - 1
# #         more = self.high + 1
# #         cur = self.low
# #         while cur < more:
# #             if self.arr[cur] < baseNum:
# #                 self.arr[less + 1], self.arr[cur] = self.arr[cur], self.arr[less + 1]
# #                 cur += 1
# #                 less += 1
# #             elif self.arr[cur] == baseNum:
# #                 cur += 1
# #             else:
# #                 self.arr[more - 1], self.arr[cur] = self.arr[cur], self.arr[more - 1]
# #                 more -= 1
# #         # print((less + 1, more))
# #         if self.k in range(less + 1, more):
# #             return self.arr[:self.k + 1]
# #         elif self.k < less + 1:
# #             self.high = less
# #             return self.splitArr(self.arr[self.low:self.high + 1])
# #             # if res is not None:
# #             #     return res
# #         else:
# #             self.low = more
# #             return self.splitArr(self.arr[self.low:self.high + 1])
# #             # if res is not None:
# #             #     return res
# #
# # for topK in range(1, 22):
# #     test = BFPRT([8, 13, 5, 7, 17, 3, 12, 6, 6, 6, 2, 6, 6, 21, 16, 4, 20, 11, 15, 10, 1, 22], topK)
# # print(test.arr)
# # res = test.do()
# # print(res)
# # print(test)
# # print(test.arr)
# # helpArr = [8, 13, 5, 7, 17, 3, 12, 6, 19, 9, 2, 14, 18, 21, 16, 4, 20, 11, 15, 10, 1, 22]
#
#
# class BFPRT(object):
#     def __init__(self, arr, k):
#         self.arr = arr
#         self.k = k - 1
#         self.low = 0
#         self.high = len(self.arr) - 1
#         helpArr = self.arr
#         self.splitArr(helpArr)
#
#     # def do(self):
#     #     helpArr = self.arr
#     #     self.splitArr(helpArr)
#         # if res is not None:
#         #     return res
#
#     def splitArr(self, helpArr):
#         # if len(helpArr) == 1:
#         #     print(self.arr[:self.k + 1])
#         #     return
#         parts = len(helpArr) // 5 if len(helpArr) % 5 == 0 else len(helpArr) // 5 + 1
#         newArr = [['']] * parts
#         for i in range(parts):
#             newArr[i] = helpArr[i * 5:i * 5 + 5]
#         return self.findMedian(newArr, parts)
#         # if res is not None:
#         #     return res
#
#     def findMedian(self, arr, parts):
#         helpArr = []
#         # print(arr, parts)
#         for i in range(parts):
#             newArr = sorted(arr[i])
#             helpArr.append(newArr[len(arr[i]) // 2])
#         # print(helpArr)
#         if len(helpArr) == 1:
#             return self.partition(helpArr[0])
#             # if res is not None:
#             #     return res
#         return self.splitArr(helpArr)
#         # if res is not None:
#         #     return res
#
#     # @staticmethod
#     # def insertSort(arr):
#     #     index = 1
#     #     while index < len(arr):
#     #         helpIndex = index
#     #         while arr[helpIndex] < arr[helpIndex - 1] and helpIndex > 0:
#     #             arr[helpIndex], arr[helpIndex - 1] = arr[helpIndex - 1], arr[helpIndex]
#     #             helpIndex -= 1
#     #         index += 1
#     #     return arr
#
#     def partition(self, baseNum):
#         # print('test')
#         # print(self.low, self.high)
#         less = self.low - 1
#         more = self.high + 1
#         cur = self.low
#         while cur < more:
#             if self.arr[cur] < baseNum:
#                 self.arr[less + 1], self.arr[cur] = self.arr[cur], self.arr[less + 1]
#                 cur += 1
#                 less += 1
#             elif self.arr[cur] == baseNum:
#                 cur += 1
#             else:
#                 self.arr[more - 1], self.arr[cur] = self.arr[cur], self.arr[more - 1]
#                 more -= 1
#         # print((less + 1, more))
#         if self.k in range(less + 1, more):
#             return self.arr[:self.k + 1]
#         elif self.k < less + 1:
#             self.high = less
#             return self.splitArr(self.arr[self.low:self.high + 1])
#             # if res is not None:
#             #     return res
#         else:
#             self.low = more
#             return self.splitArr(self.arr[self.low:self.high + 1])
#             # if res is not None:
#             #     return res
#
# import time
#
#
# time1 = time.time()
# # BFPRT 4.90710186958313
# # QuickSortTopK 2.004970073699951
# # HeapTopK 3.1659910678863525
# for topK in range(1, 1000):
#     test = BFPRT([8, 13, 5, 7, 17, 3, 12, 6, 6, 6, 2, 6, 6, 21, 16, 4, 20, 11, 15, 10, 1, 22] * 100, 2100)
#     # print(res)
# time2 = time.time()
# print(time2 - time1)
#
#

# try:
#     a = [("张三", 18), ("赵四", 19), ("王五", 20)]
#     c = {x[1]: x[2] for x in a}
#     print(c)
# except (Exception, ):
#     pass


# """
# 列表里存对象，根据对象的name属性升序排序
# """

#
# class Test:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# t1 = Test('zhao', 11)
# t2 = Test('qian', 12)
# t3 = Test('sun', 13)
# t4 = Test('li', 14)
#
# help_li = [t1, t2, t3, t4]
# help_li.sort(key=lambda x: x.name)
# for i in help_li:
#     print(i.name)


# import re
#
# string = 'boooobbbay'
# res = re.match(r'.*(b.*?b).*', string)
# print(res.group(1))

def getTalk(type="shout"):
    # We define functions on the fly
    # 定义一个函数
    def shout(word="yes"):
        return word.capitalize() + "!"

    def whisper(word="yes"):
        return word.lower() + "..."

        # Then we return one of them

    # 返回其中的而一个函数
    if type == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        # 再次注意：这里没有使用"()"，我们并没有调用函数，而是将它作为返回值返回出去
        return shout
    else:
        return whisper

        # How do you use this strange beast?


# 刚刚这函数写得那么纠结，到底有什么用呢？

# Get the function and assign it to a variable
# 调用 getTalk 函数，将返回的函数赋值给一个变量

talk = getTalk()

# You can see that "talk" is here a function object:
# 现在 "talk" 变成了一个函数对象
print(talk)
# outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
# 看下调用这个函数会返回什么
print(talk())
# outputs : Yes!

# And you can even use it directly if you feel wild:
# 当然您也可以直接调用它:
print(getTalk("whisper")())
# outputs : yes...


# A decorator is a function that expects ANOTHER function as parameter
# 装饰器是一个函数，这个函数接收一个函数作为参数
def my_shiny_new_decorator(a_function_to_decorate):
    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    # 在装饰器(decorator)内部定义了一个函数即前面提到的包装机(wrapper)
    # 这个函数在原始函数的上下添加了一些代码
    # 这些代码在原始函数调用的前后执行.

    def the_wrapper_around_the_original_function():
        # Put here the code you want to be executed BEFORE the original
        # function is called、
        # 在原始函数前面添加代码，以便在原始函数调用之前执行
        print("Before the function runs")

        # Call the function here (using parentheses)
        # 通过装饰器函数的参数调用原始函数
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original
        # function is called
        # 在原始函数的后面添加代码，以便在原始函数调用之后执行
        print("After the function runs")

        # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.

    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before
    # and after. It's ready to use!
    # 函数执行到这里，"a_function_to_decorate" 到目前为止还没有执行
    # 我们返回刚刚创建的包装函数（wrapper function）
    # 这个包装函数（wrapper function）包含那些在原始函数执行前后需要被执行的代码
    # 这个返回的包装函数（wrapper function）可以被正常调用
    return the_wrapper_around_the_original_function


# Now imagine you create a function you don't want to ever touch again.
# 加入你写了一个函数，你再也不想去碰它了
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")


a_stand_alone_function()
# outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in
# any code you want and return you a new function ready to be used:
# 为了给这个函数添加一些功能，你可以修饰（decorate）它。
# 只要将这个函数作为参数传递给一个装饰器函数，
# 那么这个装饰器函数就会动态的为这个待修饰的原始函数前后添加一些代码
# 并且返回一个新函数给你

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
# outputs:
# Before the function runs
# I am a stand alone function, don't you dare modify me
# After the function runs
