class BigRootTree(object):
    def __init__(self, arr):
        self.arr = arr

    def heapSort(self):
        if self.arr is None or len(self.arr) < 2:
            return

        for i in range(len(self.arr)):
            self.heapInsert(i)

    def heapInsert(self, index):
        while self.arr[index] > self.arr[(index - 1) // 2]:
            if (index - 1) // 2 == -1:
                break
            self.arr[index], self.arr[(index - 1) // 2] = self.arr[(index - 1) // 2], self.arr[index]
            index = (index - 1) // 2

    def heapify(self, index, heapSize):
        # heapSize的作用在于控制堆的有效部分的大小
        left = index * 2 + 1
        while left <= heapSize:
            # 这个largest为两个子孩子中较大的
            largest = left + 1 if left + 1 < heapSize and self.arr[left + 1] > self.arr[left] else left
            # 此时largest为两个子孩子中较大的与当前index中较大的
            largest = largest if self.arr[largest] > self.arr[index] else index
            if largest == index:
                break
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            index = largest
            left = index * 2 + 1


class SmallRootTree(object):
    def __init__(self, arr):
        self.arr = arr

    def heapSort(self):
        if self.arr is None or len(self.arr) < 2:
            return

        for i in range(len(self.arr)):
            self.heapInsert(i)

    def heapInsert(self, index):
        while self.arr[index] < self.arr[(index - 1) // 2]:
            if (index - 1) // 2 == -1:
                break
            self.arr[index], self.arr[(index - 1) // 2] = self.arr[(index - 1) // 2], self.arr[index]
            index = (index - 1) // 2

    def heapify(self, index, heapSize):
        # heapSize的作用在于控制堆的有效部分的大小
        left = index * 2 + 1
        while left >= heapSize:
            # 这个largest为两个子孩子中较大的
            largest = left + 1 if left + 1 > heapSize and self.arr[left + 1] < self.arr[left] else left
            # 此时largest为两个子孩子中较大的与当前index中较大的
            largest = largest if self.arr[largest] < self.arr[index] else index
            if largest == index:
                break
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            index = largest
            left = index * 2 + 1
