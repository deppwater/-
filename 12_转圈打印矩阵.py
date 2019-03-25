# 转圈打印矩阵
# 【题目】 给定一个整型矩阵matrix，请按照转圈的方式打印它。
# 例如： 1   2   3   4
#       5   6   7   8
#       9   10  11  12
#       13  14  15  16
#  打印结果为：1，2，3，4，8，12，16，15，14，13，9，5，6，7，11，10
# 【要求】 额外空间复杂度为O(1)。

"""
思路：
建立两个坐标点 左上角A坐标为(tR, tC) 右下角B坐标为(dR, dC)
先打印A点数值 然后tC+=1 一直到tC=dC
然后tR+=1 一直打印到tR=dR
然后tC-=1 一直打印到tC回归到初始值
然后tR-=1 一直打印到tR回归到初始值
最后tR+=1 tC+=1 dR-=1 dC-=1  直到tR大于dR或者tC大于dC
"""


multilist = [[0 for col in range(4)] for row in range(3)]
for i in range(3):
    for j in range(4):
        multilist[i][j] = i * 4 + j + 1


# def PrintMatrixSpiralOrder(multilist):
#     tR = 0  # 起始行
#     tC = 0  # 起始列
#     dR = len(multilist) - 1  # 终点行
#     dC = len(multilist[0]) - 1  # 终点列
#
#     # print(multilist[0])
#     # print(dR)
#     # print(dC)
#     while tR < dR and tC < dC:
#         for i in range(tC, dC):
#             print(multilist[tR][i])
#         for i in range(tR, dR):
#             print(multilist[i][dC])
#         for i in range(dC, tC, -1):
#             print(multilist[dR][i])
#         for i in range(dR, tR, -1):
#             print(multilist[i][tC])
#         tR += 1
#         tC += 1
#         dR -= 1
#         dC -= 1
#
#
# PrintMatrixSpiralOrder(multilist)

print(multilist)


def PrintMatrixSpiralOrder(multilist):
    tR = 0  # 起始行
    tC = 0  # 起始列
    dR = len(multilist) - 1  # 终点行
    dC = len(multilist[0]) - 1  # 终点列
    while tR <= dR and tC <= dC:
        for i in range(tC, dC):
            print(multilist[tR][i])
        for i in range(tR, dR):
            print(multilist[i][dC])
        for i in range(dC, tC, -1):
            print(multilist[dR][i])
        for i in range(dR, tR, -1):
            print(multilist[i][tC])
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1


PrintMatrixSpiralOrder(multilist)