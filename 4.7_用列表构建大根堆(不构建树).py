"""
思路：
要使整体上成为大根堆 那么先假设0~(n-1)位置上的数已经形成大根堆
现在想让n位置上的数加入这个大根堆
首先比较n位置上的数跟自己的父节点上的数的大小 即index为(i-1)//2位置上的数
如果n位置上的数更大 那么进行交换
重复上述操作直到小于等于的时候停止
这里有个细节就是当到达0位置的时候 0位置会跟(0-1)//2即0位置的数再比较一次 那么结果就是相等
所以终止条件为小于等于

时间复杂度：
由于每个新加入的数只需要跟自己的父节点以及父节点的父节点进行比较
所以每次的调整代价为O(logN)
那么当有N个数的时候 每个节点加入并构成二叉树的复杂度为O(log1) + O(log2) + O(log3) + ... + O(log(N-1))
因此最终(建立一个大根堆)的复杂度为O(N)

heapify：
当数组中的一个数变大的时候 只需要跟自己的父节点进行比较即可 这个过程就是构建大根堆的过程
而当数组中的一个数变小的时候 它则需要跟自己的左子节点和右子节点同时比较
如果两个子节点有任何一个节点比该节点大 那么该节点跟子节点中较大的数进行交换
有点像反向构建大根堆的过程
"""


def heapSort(arr):
    if arr is None or len(arr) < 2:
        return

    for i in range(len(arr)):
        heapInsert(arr, i)


def heapInsert(arr, index):
    while arr[index] > arr[(index - 1) // 2]:
        if (index - 1) // 2 == -1:
            break
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2


arr1 = [2, 1, 3, 6, 0, 4, 3, 3]
heapSort(arr1)
print(arr1)


def heapify(arr, index, heapSize):
    # heapSize的作用在于控制堆的有效部分的大小
    left = index * 2 + 1
    while left <= heapSize:
        # 这个largest为两个子孩子中较大的
        largest = left + 1 if left + 1 < heapSize and arr[left + 1] > arr[left] else left
        # 此时largest为两个子孩子中较大的与当前index中较大的
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        arr[index], arr[largest] = arr[largest], arr[index]
        index = largest
        left = index * 2 + 1


arr2 = [7, 5, 4, 3, 5, 2]
heapify(arr2, 0, 5)
print(arr2)
