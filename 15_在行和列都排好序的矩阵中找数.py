# 在行列都排好序的矩阵中找数
# 【题目】 给定一个有N*M的整型矩阵matrix和一个整数K，
# matrix的每一行和每一 列都是排好序的。实现一个函数，判断K
# 是否在matrix中。 例如： 0 1 2 5 2 3 4 7 4
# 4 4 8 5 7 7 9 如果K为7，返回true；如果K为6，返
# 回false。
# 【要求】 时间复杂度为O(N+M)，额外空间复杂度为O(1)

"""
思路：
从右上角位置开始找 因为整体是排好序的 如果要找的数比当前坐标位置的数小 那么坐标向左移动一格 如果大 则向下移动一格
因为是从右上角开始的 所以边界判断为纵坐标是否小于0以及横坐标是否大于整体行数
"""


def FindNumInSortedMatrix(num):
    multilist = [[0, 1, 2, 5], [2, 3, 4, 7], [4, 4, 4, 8], [5, 7, 7, 9]]
    print(multilist)
    aR = 0  # a起始行
    dR = len(multilist) - 1  # 终点行
    aC = len(multilist[0]) - 1  # 起点列
    while aC >= 0 or aR <= dR:
        if num < multilist[aR][aC]:
            aC -= 1
        elif num > multilist[aR][aC]:
            aR += 1
        if aC < 0 or aR > dR:
            return False
        elif num == multilist[aR][aC]:
            return True


result = FindNumInSortedMatrix(-1)
print(result)