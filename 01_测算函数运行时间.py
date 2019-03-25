import timeit


def text1():
    li = []
    for i in range(10000):
        li.append(i)


def text2():
    li = []
    for i in range(10000):
        li += [i]


def text3():
    li = [i for i in range(10000)]


def text4():
    li = list(range(10000))


def text5():
    li = []
    for i in range(10000):
        li.extend([i])


def text6():
    li = []
    for i in range(10000):
        li = li + [i]


def text7():
    li = []
    for i in range(10000):
        li.insert(0, i)


time1 = timeit.Timer('text1()', 'from __main__ import text1')
print('append:%.2f' % time1.timeit(number=1000))

time2 = timeit.Timer('text2()', 'from __main__ import text2')
print('+=:%.2f' % time2.timeit(number=1000))

time3 = timeit.Timer('text3()', 'from __main__ import text3')
print('[i for i in range]:%.2f' % time3.timeit(number=1000))

time4 = timeit.Timer('text4()', 'from __main__ import text4')
print('list(range):%.2f' % time4.timeit(number=1000))

time5 = timeit.Timer('text5()', 'from __main__ import text5')
print('extend:%.2f' % time5.timeit(number=1000))

time6 = timeit.Timer('text6()', 'from __main__ import text6')
print('+:%.2f' % time6.timeit(number=1000))


