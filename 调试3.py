# “之”字形打印矩阵
# 【题目】 给定一个矩阵matrix，按照“之”字形的方式打印这
# 个矩阵，例如： 1 2 3 4 5 6 7 8 9 10 11 12
# “之”字形打印的结果为：1，2，5，9，6，3，4，7，10，11，
# 8，12
# 【要求】 额外空间复杂度为O(1)。


multilist = [[0 for col in range(4)] for row in range(4)]
for i in range(4):
    for j in range(4):
        multilist[i][j] = i * 4 + j + 1
print(multilist)


def zigzagPrintMatrix(multilist):
    aR = 0  # a起始行 先向下
    aC = 0  # a起始列 先向下
    bR = 0  # b起始行 先向右
    bC = 0  # b起始列 先向右
    dR = len(multilist) - 1  # 终点行
    dC = len(multilist[0]) - 1  # 终点列
    # terminal = 0
    boolean = True
    # if aR <= dR or aC <= bC:
    #     terminal = min(aR, bC)
    # else:
    #     terminal = min(dR, dC) - min(aC, bR)
    while aC <= dC:
        if aC == 0 and bR == 0:
            if boolean:
                for i in range(min(aR, bC) + 1):
                    # print(aR - i, i)
                    # print('=====true=====')
                    print(multilist[aR - i][i])
            if not boolean:
                for i in range(min(aR, bC) + 1):
                    # print(i, bC - i)
                    # print('=====false=====')
                    print(multilist[i][bC - i])
            if aR < dR:
                aR += 1
            else:
                aC += 1
            if bC < dC:
                bC += 1
            else:
                bR += 1
            boolean = not boolean
        else:
            # print('测试')
            if boolean:
                for i in range((min(dR, dC) - min(aC, bR)), -1, -1):
                    # print(min(dR, dC) - min(aC, bR)
                    # print('=====true=====')
                    print(multilist[bR + i][dC - i])
            if not boolean:
                for i in range((min(dR, dC) - min(aC, bR)), -1, -1):
                    # print(min(dR, dC) - min(aC, bR)
                    # print('=====false=====')
                    print(multilist[dR - i][aC + i])
            aC += 1
            bR += 1
            boolean = not boolean

zigzagPrintMatrix(multilist)
