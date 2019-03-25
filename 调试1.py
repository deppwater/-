# print(2 ** 32)
# 4294967296

# import random
#
#
# a = []
# for i in range(1,11):
#     a.append(i)
# random.shuffle(a)
# print(a)
#
#
# [8 < 7 < 5 > 10 < 2 > 3 > 4 < 1 > 9 < 6]
# [5 > 8 > 7 > 10 < 3 < 4 < 2 < 9 < 6 < 1]
# [5 > 7 > 8 > 10 < 4 < 3 < 9 < 6 < 2 < 1]

# a = {'xiaoming': 80, 'huang': 60, 'li': 70}
#
# res = sorted(a.values(), key=lambda x: x)
# print(res)


a = "wtf!"

b = "wtf!"


# print(id(a))
# print(id(b))
# print('a' * 20 is 'aaaaaaaaaaaaaaaaaaaa')


def some_func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'


res = some_func()


# print(res)


class WTF(object):
    def __init__(self): print("I")

    def __del__(self): print("D")


# print(WTF() == WTF())
# print(id(WTF()) == id(WTF()))


array_2 = [1, 2, 3, 4]
g2 = (x for x in array_2)
array_2 = [1, 2, 3, 4, 5]

# print(array_2)
# print(list(g2))


# 这是一种特别为交互式环境做的编译器优化. 当你在实时解释器中输入两行的时候, 他们会单独编译, 因此也会单独进行优化.
# 如果你在 .py 文件中尝试这个例子, 则不会看到相同的行为, 因为文件是一次性编译的.
c = 256
d = 256
# print(c is d)

c = 257
d = 257
# print(c is d)

# print(r"\C:\")

from datetime import datetime

midnight = datetime(2018, 1, 1, 0, 0)
midnight_time = midnight.time()

# if midnight_time:
# print("Time at midnight is", midnight_time)


# print(isinstance(True, int))


some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])

another_tuple[2].append(1000)
try:
    another_tuple[2] += [99, 999]
finally:
    print(another_tuple)