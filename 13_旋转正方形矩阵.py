# 【题目】 给定一个整型正方形矩阵matrix，请把该矩阵调整成
# 顺时针旋转90度的样子。
# 【要求】 额外空间复杂度为O(1)。

"""
思路：
建立两个坐标点 左上角A坐标为(tR, tC) 右下角B坐标为(dR, dC)
A、右上角的点、B、左下角的点 四个点相互交换位置
A纵坐标+1 右上角的点横坐标+1 B纵坐标-1 左下角的点横坐标-1
然后继续交换 次数为dR与tR的差值
交换完毕后 tR+=1 tC+=1 dR-=1 dC-=1
循环直到 tR<dR 且 tC<dC
"""


multilist = [[0 for col in range(4)] for row in range(4)]
for i in range(4):
    for j in range(4):
        multilist[i][j] = i * 4 + j + 1

print(multilist)


def ReverseList(multilist):
    tR = 0  # 起始行
    tC = 0  # 起始列
    dR = len(multilist) - 1  # 终点行
    dC = len(multilist[0]) - 1  # 终点列
    count = 0
    # print(dR)
    # print(dC)
    while tR < dR and tC < dC:
        times = dC - tC
    # print(multilist)
        for i in range(times):
            multilist[tR][i + count], multilist[i + count][dC], multilist[dR][times - i + count], multilist[times - i + count][tC] \
                = multilist[times - i + count][tC], multilist[tR][i + count], multilist[i + count][dC], multilist[dR][times - i + count]
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1
        count += 1
    print(multilist)
    # times = dC - tC
    # for i in range(times):
    #     multilist[tR][i + 1], multilist[i + 1][dC], multilist[dR][times - i + 1], multilist[times - i + 1][tC] \
    #         =multilist[times - i + 1][tC], multilist[tR][i + 1], multilist[i + 1][dC], multilist[dR][times - i + 1]
    # print(multilist)

    # count += 1
    # print(count)
    # print(multilist)

ReverseList(multilist)
