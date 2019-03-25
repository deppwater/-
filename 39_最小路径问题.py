# 给你一个二维数组，二维数组中的每个数都是整数，要求从左上角走到右下角，每一步只能向右或向下。沿途经过的数字要累加起来。返回最小的路径和。
"""
由于整个过程中包含了所有的情况 所以是枚举而不是贪心
"""

multilist = [[0 for col in range(4)] for row in range(4)]
multilist[0] = [1, 3, 5, 9]
multilist[1] = [8, 1, 3, 4]
multilist[2] = [5, 0, 6, 1]
multilist[3] = [8, 8, 4, 0]

print(multilist)


def minPath(multilist, i, j):
    # i是行数 j是列数
    if i == len(multilist) - 1 and j == len(multilist[0]) - 1:
        # 这里判断如果到达右下角直接返回右下角的值给上一层递归用于累加
        return multilist[i][j]

    if i == len(multilist) - 1:
        return multilist[i][j] + minPath(multilist, i, j + 1)

    if j == len(multilist[0]) - 1:
        return multilist[i][j] + minPath(multilist, i + 1, j)

    # 右边的一个位置到右下角最短路径的和
    # 由于是递归所以所有可能性都包括在内
    right = minPath(multilist, i, j + 1)
    # 下边的一个位置到右下角最短路径的和
    down = minPath(multilist, i + 1, j)
    return multilist[i][j] + min(right, down)


res = minPath(multilist, 0, 0)
print(res)
