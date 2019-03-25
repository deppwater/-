import numpy
"""
对数的基本概念如下：
有一个你想测试的算法a
实现一个绝对正确但复杂度高的算法b
实现一个随机样本产生器
实现比对算法a和b的方法
多次（100000+）比对a和b来验证a是否正确
如果有样本出错，则打印出来分析
当对此对比测试都正确时，可以基本判断算法a正确

注意：
如果不确定rightMethod方法是否正确可以把两种方法的结果都打印出来
笔试的时候准备数组或者树等的对数器来验证代码
"""


def generateRandomArray(value, size):
    """
    生成最大数量为size 最大值为value的随机数组
    :return:
    """
    arr = list()
    for i in range(int((size + 1) * numpy.random.rand())):
        arr.append(int((value + 1) * (numpy.random.rand())))
    return arr


def rightMathod(arr):
    """
    绝对正确的方法
    :return:
    """
    arr.sort()
    return arr


def mainTest(times, method):
    size = 10
    value = 100
    for i in range(times):
        arr1 = generateRandomArray(size, value)
        arr2 = arr1
        arr3 = arr1
        result1 = method(arr1)
        result2 = rightMathod(arr2)
        if result1 != result2:
            succeed = False
            print(arr3)
            print(succeed)
            break
