# “之”字形打印矩阵
# 【题目】 给定一个矩阵matrix，按照“之”字形的方式打印这
# 个矩阵，例如： 1 2 3 4 5 6 7 8 9 10 11 12
# “之”字形打印的结果为：1，2，5，9，6，3，4，7，10，11，
# 8，12
# 【要求】 额外空间复杂度为O(1)。


# multilist = [[0 for col in range(5)] for row in range(3)]
# for i in range(3):
#     for j in range(5):
#         multilist[i][j] = i * 5 + j + 1
# print(multilist)
#
#
# def zigzagPrintMatrix(multilist):
#     aR = 0  # a起始行 先向下
#     aC = 0  # a起始列 先向下
#     bR = 0  # b起始行 先向右
#     bC = 0  # b起始列 先向右
#     dR = len(multilist) - 1  # 终点行
#     dC = len(multilist[0]) - 1  # 终点列
#     # terminal = 0
#     boolean = True
#     # if aR <= dR or aC <= bC:
#     #     terminal = min(aR, bC)
#     # else:
#     #     terminal = min(dR, dC) - min(aC, bR)
#     while aC <= dC:
#         if aC == 0 and bR == 0:
#             if boolean:
#                 for i in range(min(aR, bC) + 1):
#                     # print(aR - i, i)
#                     # print('=====true=====')
#                     print(multilist[aR - i][i])
#             if not boolean:
#                 for i in range(min(aR, bC) + 1):
#                     # print(i, bC - i)
#                     # print('=====false=====')
#                     print(multilist[i][bC - i])
#             if aR < dR:
#                 aR += 1
#             else:
#                 aC += 1
#             if bC < dC:
#                 bC += 1
#             else:
#                 bR += 1
#             boolean = not boolean
#         else:
#             # print('测试')
#             if boolean:
#                 for i in range((min(dR, dC) - min(aC, bR)), -1, -1):
#                     # print(min(dR, dC) - min(aC, bR)
#                     # print('=====true=====')
#                     print(multilist[bR + i][dC - i])
#             if not boolean:
#                 for i in range((min(dR, dC) - min(aC, bR)), -1, -1):
#                     # print(min(dR, dC) - min(aC, bR)
#                     # print('=====false=====')
#                     print(multilist[dR - i][aC + i])
#             aC += 1
#             bR += 1
#             boolean = not boolean
#
#
# zigzagPrintMatrix(multilist)

"""
思路：
给定三个坐标点 A点坐标值(aR, aC) B点坐标值(bR, bC) D点坐标值(dR, dC) 其中A、B起始在(0, 0)位置 D点为右下角坐标
A点先向下移动再向右移动 B点先向右移动再向下移动 直到A或B达到D位置
移动的同时打印A、B之间的数 以一个bool值来控制方向
"""

multilist1 = [[0 for col1 in range(3)] for row1 in range(5)]
for i in range(5):
    for j in range(3):
        multilist1[i][j] = i * 3 + j + 1
print(multilist1)


multilist2 = [[0 for col2 in range(5)] for row2 in range(3)]
for i in range(3):
    for j in range(5):
        multilist2[i][j] = i * 5 + j + 1
print(multilist2)


def zigzagPrintMatrix(multilist):
    aR = 0  # a起始行 先向下
    aC = 0  # a起始列 先向下
    bR = 0  # b起始行 先向右
    bC = 0  # b起始列 先向右
    dR = len(multilist) - 1  # 终点行
    dC = len(multilist[0]) - 1  # 终点列
    boolean = True
    while aC <= dC:
        if boolean:
            for i in range(abs(aC - bC) + 1):
                print(multilist[aR - i][aC + i])
        if not boolean:
            for i in range(abs(aC - bC) + 1):
                print(multilist[bR + i][bC - i])
        boolean = not boolean
        if bC <= dC - 1:
            bC += 1
        else:
            bR += 1
        if aR <= dR - 1:
            aR += 1
        else:
            aC += 1

zigzagPrintMatrix(multilist1)
print('=' * 30)
zigzagPrintMatrix(multilist2)
