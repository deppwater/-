from extra.singleListNode import *

text = SingleLinkList(1)
text.append(3)
text.append(5)
text.append(7)
text.append(8)
text.append(6)
text.append(4)
text.append(2)
text.append(4)
text.append(2)
text.append(0)


def makeTravelListNode(headNode):
    curNode = headNode
    curNode = curNode.next
    while curNode.next is not None:
        curNode.pre = curNode
        curNode = curNode.next


def getLast(headNode):
    curNode = headNode
    while curNode.next is not None:
        curNode = curNode.next
    return curNode


def getLength(headNode):
    if headNode:
        cur = 1
    else:
        return 0
    cur_node = headNode
    while cur_node.next is not None:
        cur_node = cur_node.next
        cur += 1
    return cur


def heapSort(headNode):
    # help_li = list()
    heapSize = getLength(headNode) - 1
    curNode = getLast(headNode)
    heapNode = getLast(headNode)
    if heapSize < 2:
        return headNode

    for i in range(heapSize + 1):
        heapInsert(headNode, heapNode)
        headNode = headNode.next

    while heapSize > 0:
        headNode, curNode = curNode, headNode
        # help_li.insert(0, arr.pop(-1))
        heapSize -= 1
        curNode = curNode.pre
        heapify(headNode, 0, heapSize)

    # help_li.insert(0, arr[0])
    # return help_li
    return headNode


def heapInsert(headNode, heapNode):
    while heapNode.elem > arr[(index - 1) // 2]:
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