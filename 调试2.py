# a = dict.fromkeys(range(5), [])
# b = [1, 2, 3, 4, 5]
# a[0] = [5]
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))
# print(a)


# 相当于3*2^2
# print(3 << 2)

# for i in range(10, -1):
#     print(i)

# print(1 // 2)

# help = [None] * (11)
# print(help)

# print([] + [] + [1])
# import random
# for i in range(100):
#     print(random.randint(1, 10))

# for i in range(6):
#     print((i - 1) // 2)


# arr = [1, 2, 3, 4]
# arr.pop()
# print(arr)


# import queue as Q
#
#
# class Skill(object):
#     def __init__(self, priority, description):
#         self.priority = priority
#         self.description = description
#
#     def __lt__(self, other):
#         return self.description < other.description
#
#     def __str__(self):
#         return '(' + str(self.priority) + ',\'' + self.description + '\')'
#
#
# def PriorityQueue_class():
#     que = Q.PriorityQueue()
#     que.put(Skill(7, 'proficient7'))
#     que.put(Skill(5, 'proficient5'))
#     que.put(Skill(6, 'proficient6'))
#     que.put(Skill(10, 'expert'))
#     que.put(Skill(1, 'novice'))
#     print('end')
#     while not que.empty():
#         print(que.get())
#
#
# PriorityQueue_class()

# for i in reversed(range(10)):
#     print(i)

# arr = 10 * []
# print(arr[6])

# arr = [[]]*10
# print(arr)
# # arr1 = []
# # arr1[9] = 1
# # print(arr1)
# arr[0] = 1
# print(arr)
# if not arr[1]:
#     print('text')

# ex = Exception('text')
# raise ex
# class dog:
#     def eat(self):
#         print('text')
#
# dog1 = dog()
# dog1.eat()
# print(dog1)

#
# class Node(object):
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#
# node1 = Node(1)
# node2 = Node(2)
# # import queue
# # q = queue.Queue()
# # q.put(dog1)
# # a = q.get()
# # print(a)
# # print(a.eat())
#
#
# deit = {}
# deit[node1] = node2
#
# print(deit[node1])

from collections import namedtuple
from io import StringIO
import math

# define the node structure
Node = namedtuple('Node', ['data', 'left', 'right'])
# initialize the tree
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, b):
        self.queue.insert(0, b)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []


def getheight(node):
    if not node:
        return 0
    else:
        return max(getheight(node.left), getheight(node.right)) + 1


def add_padding(str, pad_length_value):
    str = str.strip()
    return str.center(pad_length_value, ' ')


# sotre node , space and slashes in list first, then print out
def pretty_print(tree):
    output = StringIO()
    pretty_output = StringIO()

    current_level = Queue()
    next_level = Queue()
    current_level.enqueue(tree)
    depth = 0

    # get the depth of current tree
    # get the tree node data and store in list
    if tree:
        while not current_level.isEmpty():
            current_node = current_level.dequeue()
            output.write('%s ' % current_node.data if current_node else 'N ')
            next_level.enqueue(
                current_node.left if current_node else current_node)
            next_level.enqueue(
                current_node.right if current_node else current_node)

            if current_level.isEmpty():
                if sum([i is not None for i in next_level.queue]
                       ):  # if next level has node
                    current_level, next_level = next_level, current_level
                    depth = depth + 1
                output.write('\n')
    print('the tree print level by level is :')
    print(output.getvalue())
    print("current tree's depth is %i" % (depth + 1))

    # add space to each node
    output.seek(0)
    pad_length = 3
    keys = []
    spaces = int(math.pow(2, depth))

    while spaces > 0:
        skip_start = spaces * pad_length
        skip_mid = (2 * spaces - 1) * pad_length

        key_start_spacing = ' ' * skip_start
        key_mid_spacing = ' ' * skip_mid

        keys = output.readline().split(' ')  # read one level to parse
        padded_keys = (add_padding(key, pad_length) for key in keys)
        padded_str = key_mid_spacing.join(padded_keys)
        complete_str = ''.join([key_start_spacing, padded_str])

        pretty_output.write(complete_str)

        # add space and slashes to middle layer
        slashes_depth = spaces
        print('current slashes depth im_resize:')
        print(spaces)
        print("current levle's list is:")
        print(keys)
        spaces = spaces // 2
        if spaces > 0:
            pretty_output.write('\n')  # print '\n' each level

            cnt = 0
            while cnt < slashes_depth:
                inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                symbol_start_spacing = ' ' * (skip_start - cnt - 1)
                symbol_mid_spacing = ' ' * (skip_mid - 2 * (cnt + 1))
                pretty_output.write(''.join([symbol_start_spacing, symbol]))
                for i in keys[1:-1]:
                    pretty_output.write(''.join([symbol_mid_spacing, symbol]))
                pretty_output.write('\n')
                cnt = cnt + 1

    print(pretty_output.getvalue())


if __name__ == '__main__':
    pretty_print(tree)
