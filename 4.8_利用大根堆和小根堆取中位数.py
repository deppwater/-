"""
题目要求：
有一个不断吐出数的流 这些数是不规则的 要求在任意时刻都能拿到这个数组中的中位数(当中位有两个数的时候取平均数)

思路：
构建一个大根堆和一个小跟堆 每吐出一个数就往里加入
假设第一个数进入大根堆 自己构成一个大根堆的顶部
那么接下来的数如果小于大根堆的顶部 就加入大根堆 反之加入小根堆
除此之外要保证两者长度差不能超过1
如果大根堆比小根堆长超过1 那么从大根堆的顶部弹出一个数加入小跟堆
并且大根堆的最后一个数变成大根堆的顶部 进行一个heapify过程重新形成大根堆
反之则从小根堆顶部弹出一个数加入大根堆 小根堆最后一个数变成小根堆顶部 进行一个heapify过程
最终形成的小根堆与大根堆长度基本相等 那么大根堆里的数就是整体较小的那一半 小根堆则为整体较大的那一半
则顶部的一个或两个数的平均数就为整体的平均数

补充：
由于每次进行插入排序操作只用管一条链上的数 所以调整堆的时间复杂度为O(logN)
而用常规办法先加入数组排序然后求中位数的时间复杂度为排序的时间复杂度 即O(N·logN)
"""

max_heap_li = list()
min_heap_li = list()


def add(num):
    # heapSizeMax = len(max_heap_li) - 1
    # heapSizeMin = len(min_heap_li) - 1
    if not max_heap_li and not min_heap_li:
        max_heap_li.append(num)
    else:
        if num <= max_heap_li[0]:
            max_heap_li.append(num)
            heapInsertMax(max_heap_li, len(max_heap_li) - 1)
        else:
            min_heap_li.append(num)
            heapInsertMin(min_heap_li, len(min_heap_li) - 1)
    DValue = len(max_heap_li) - len(min_heap_li)
    if abs(DValue) > 1:
        if DValue > 1:
            max_heap_li[0], max_heap_li[-1] = max_heap_li[-1], max_heap_li[0]
            trans_num = max_heap_li.pop(-1)
            heapSizeMax = len(max_heap_li) - 1
            heapifyMax(max_heap_li, 0, heapSizeMax)
            min_heap_li.append(trans_num)
            heapInsertMin(min_heap_li, len(min_heap_li) - 1)
        else:
            min_heap_li[0], min_heap_li[-1] = min_heap_li[-1], min_heap_li[0]
            trans_num = min_heap_li.pop(-1)
            # heapSizeMin定义位置有问题
            heapSizeMin = len(min_heap_li) - 1
            heapifyMin(min_heap_li, 0, heapSizeMin)
            max_heap_li.append(trans_num)
            heapInsertMax(max_heap_li, len(max_heap_li) - 1)


def heapInsertMax(arr, index):
    # if index == -1:
    #     index = len(arr) - 1
    while arr[index] > arr[(index - 1) // 2]:
        if (index - 1) // 2 == -1:
            break
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]


def heapifyMax(arr, index, heapSize):
    left = index * 2 + 1
    while left <= heapSize:
        largest = left + 1 if left + 1 < heapSize and arr[left + 1] > arr[left] else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        arr[index], arr[largest] = arr[largest], arr[index]
        index = largest
        left = index * 2 + 1


def heapInsertMin(arr, index):
    # if index == -1:
    #     index = len(arr) - 1
    while arr[index] < arr[(index - 1) // 2]:
        if (index - 1) // 2 == -1:
            break
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]


def heapifyMin(arr, index, heapSize):
    left = index * 2 + 1
    while left <= heapSize:
        smallest = left + 1 if left + 1 < heapSize and arr[left + 1] < arr[left] else left
        smallest = smallest if arr[smallest] < arr[index] else index
        if smallest == index:
            break
        arr[index], arr[smallest] = arr[smallest], arr[index]
        index = smallest
        left = index * 2 + 1


def printOut():
    print(max_heap_li)
    print(min_heap_li)
    if len(max_heap_li) == len(min_heap_li):
        return (max_heap_li[0] + min_heap_li[0]) / 2
    elif len(max_heap_li) > len(min_heap_li):
        return max_heap_li[0]
    else:
        return min_heap_li[0]


add(1)
add(2)
add(3)
add(4)
add(5)
add(6)
add(8)
add(0)
add(9)
result = printOut()
print(result)
