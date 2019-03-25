# help_li = []
# index = 0
#
#
# def printAllPermutations1(arr, i):
#     print('test')
#     # print(arr)
#     help_arr = arr[:]
#
#     if i == len(arr):
#         # print(arr)
#         return
#     j = 0
#
#     while j < len(arr):
#         # print(arr)
#         # help_arr = arr[:]
#         # print(help_arr)
#         help_arr[i], help_arr[j] = help_arr[j], help_arr[i]
#         help_li.append(help_arr[:])
#         print(help_arr)
#         # help_arr[0], help_arr[1] = help_arr[1], help_arr[0]
#         # help_li.append(help_arr)
#
#         # arr[i], arr[j] = arr[j], arr[i]
#         j += 1
#     printAllPermutations1(arr, i + 1)
#     # printAllPermutations1(arr, i + 1)
#
#
# # def printAllPermutations2():
# #     """
# #     去重
# #     :return:
# #     """
# #     pass
#
#
# printAllPermutations1([1, 2, 3], 0)
# print(len(help_li))
# a = set()
# for i in help_li:
#     a.add(tuple(i))
# print(a)


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = 4
print(node1.next)
node2 = node3
print(node1.next)
print(node2.elem)
