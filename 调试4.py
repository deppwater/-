# lis1 = [1, 2, 3, 4, 5, 6, 7]
# # lis2 = [6, 7, 1, 2, 3, 4, 5]
#
# list1 = []
# for x in range(5):
#     def inner():  # x=x
#         return 'text'
#
#     list1.append(inner)
#
# print(id(list1[0]))
# print(id(list1[1]))
#
# a = 'abcdefghijklmnopqrstuvwxyz'
# for i in a:
#     print(ord(i) - ord('a'))


# from extra.rootTree import BigRootTree, SmallRootTree
#
# test = BigRootTree([1, 5, 4, 3, 5, 2])
# test.heapSort()
# print(test.arr)
#
#
# test2 = SmallRootTree([10, 20, 30])
# test2.heapSort()
# print(test2.arr)
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        pass


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

print(node1.elem)

import heapq

c = [13, 5, 7, 8, 2, 4]
heap = [node1.elem, node2.elem, node3.elem, node4.elem, node5.elem]
a = []
# heapq.heapify(a)
# print(a)
# b = heapq.heappush(a, c)
print(heapq.nlargest(3, heap))
print(heap)

d = [{1: [10, 20]}, {2: [20, 30]}, {3: [30, 40]}]
res = heapq.nlargest(2, d, key=lambda s: list(s.values())[0][0])
print(res)
