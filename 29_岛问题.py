# 岛问题
# 一个矩阵中只有0和1两种值，每个位置都可以和自己的上、下、左、右
# 四个位置相连，如果有一片1连在一起，这个部分叫做一个岛，求一个
# 矩阵中有多少个岛？
# 举例：
# 0 0 1 0 1 0
# 1 1 1 0 1 0
# 1 0 0 1 0 0
# 0 0 0 0 0 0
# 这个矩阵中有三个岛。

"""
常规解法思路：
从头(左上角)开始遍历 当遍历到1的时候进入感染函数 进入感染函数之前岛数+1
感染函数是个递归过程 递归的将所有跟这个1连成一片的数改成2

优化思路：
利用分治和并查集的思想 达到多核处理 即本来是单核处理 现在分成2^n块交给2^n个计算机分别计算出结果后再进行合并达到提高效率的效果
假设将上面的岛分成四块
先计算出每块各自的岛的数量 重点在于合并过程
合并时需要收集每块岛的边界信息
当两个岛相邻的边上左右都为1时 进行合并操作
即利用并查集将本来单独的两个集合合并为一个集合 然后总岛数-1
这样做的好处在于下次再碰到本来分属这两个集合的1连在一起时
可以通过寻找各自的代表节点 会发现这两个本来分属两个集合的由于合并操作现在的代表节点相同
"""

multilist = [[0 for col in range(6)] for row in range(4)]
multilist[0][2] = 1
multilist[0][4] = 1
multilist[1][0] = 1
multilist[1][1] = 1
multilist[1][2] = 1
multilist[1][4] = 1
multilist[2][0] = 1
multilist[2][3] = 1
# multilist[2][4] = 1

for k in range(4):
    print(multilist[k])
print('')


def countIslands(m):
    row = len(m)  # 行数
    column = len(m[0])  # 列数
    result = 0
    for i in range(row):
        for j in range(column):
            if m[i][j] == 1:
                result += 1
                infect(m, i, j, row, column)
    return result


def infect(m, i, j, row, column):
    if i < 0 or i > row or j < 0 or j > column or m[i][j] != 1:
        return
    m[i][j] = 2
    infect(m, i + 1, j, row, column)
    infect(m, i - 1, j, row, column)
    infect(m, i, j + 1, row, column)
    infect(m, i, j - 1, row, column)


res = countIslands(multilist)
print(res)
