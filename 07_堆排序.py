"""
思路：
先将数组构建成大根堆 然后将堆顶的数弹出并加入一个新的数组的最后一位
再将大根堆的最后一位变成大根堆的堆顶 heapSize减1 然后进行一个heapify的操作
重复上述操作 则可以进行排序

最差时间复杂度 ---- O(nlogn)
最优时间复杂度 ---- O(nlogn)
平均时间复杂度 ---- O(nlogn)
所需辅助空间 ------ O(1)
稳定性 ----------- 不稳定

堆结构非常重要
1，堆结构的heapInsert与heapify
2，堆结构的增大和减少
3，如果只是建立堆的过程，时间复杂度为O(N)
4，优先级队列结构，就是堆结构
"""
import extra


def heapSort(arr):
    # help_li = list()
    heapSize = len(arr) - 1
    if len(arr) < 2:
        return arr

    for i in range(len(arr)):
        heapInsert(arr, i)

    while heapSize > 0:
        arr[0], arr[heapSize] = arr[heapSize], arr[0]
        # help_li.insert(0, arr.pop(-1))
        heapSize -= 1
        heapify(arr, 0, heapSize)

    # help_li.insert(0, arr[0])
    # return help_li
    return arr


def heapInsert(arr, index):
    while arr[index] > arr[(index - 1) // 2]:
        if (index - 1) // 2 == -1:
            break
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2


def heapify(arr, index, heapSize):
    left = index * 2 + 1
    while left <= heapSize:
        largest = left + 1 if left + 1 <= heapSize and arr[left + 1] > arr[left] else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = index * 2 + 1


arr1 = [1, 2, 4, 7, 3, 6, 4, 5]
result = heapSort(arr1)
print(result)
# arr1.sort()
# print(arr1)
# 用对数器验证
extra.Testing.mainTest(10000, heapSort)
