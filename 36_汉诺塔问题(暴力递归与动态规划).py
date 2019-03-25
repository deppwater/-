"""
思路：
假设题目要求将n个数据从from挪到to上 并提供一个help
那么问题可以简化为
先将(n-1)个数据从from挪到help上
然后将from上剩下的n数据挪到to上
再把help上(n-1)数据挪到to上
递归的求(n-1)的过程即可


暴力递归：
1，把问题转化为规模缩小了的同类问题的子问题 
2，有明确的不需要继续进行递归的条件(base case) 
3，有当得到了子问题的结果之后的决策过程
4，不记录每一个子问题的解

动态规划 
1，从暴力递归中来 
2，将每一个子问题的解记录下来，避免重复计算
3，把暴力递归的过程，抽象成了状态表达 
4，并且存在化简状态表达，使其更加简洁的可能
"""


def Hanio(N, hanioFrom, hanioTo, hanioHelp):
    """
    :param N: 代表是1-N的问题
    :return:
    """
    if N == 1:
        print(hanioFrom, '--->', hanioTo)
    else:
        # 因为第一步是将(n-1)个数据从from挪到help上
        # 因此问题的规模是(n-1) 所以N应该就为(n-1)
        Hanio(N - 1, hanioFrom, hanioHelp, hanioTo)
        # 第二步是将from上剩下的一个n数据挪到to上
        # 因此问题的规模是1 所以此处N应该为1
        Hanio(1, hanioFrom, hanioTo, hanioHelp)
        # 第三步把help上(n-1)数据挪到to上
        # 那么问题的规模仍然是(n-1)
        Hanio(N - 1, hanioHelp, hanioTo, hanioFrom)


Hanio(8, 'a', 'c', 'b')
"""
因为时间复杂度:
T(N) = T(N - 1) + 1 + T(N - 1)
即 T(N) = 2T(N - 1) + 1
因此总步数为 2^N - 1
复杂度为O(2^N)
"""
