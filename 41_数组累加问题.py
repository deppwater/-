# 给你一个数组arr，和一个整数aim。如果可以任意选择arr中的数字，能不能累加得到aim，返回true或者false。

"""
这道题的动态规划表：
由于变化的只有i和sum_num 那么这个表的纵坐标就为i 横坐标为arr中所有的数之和
所有的返回值一定能装在这个表内
假设数组为[3, 2, 5] aim为7 那么表为
  0 1 2 3 4 5 6 7 8 9 10
0 T F T F T T F T F F F
1 T F T F F T F T F F F
2 F F T F F F F T F F F
3 F F F F F F F T F F F
每个坐标点表示起始值如果为纵坐标对应的值 那么是否能得到结果7
"""


def isSum(arr, i, sum_num, aim):
    if i == len(arr):
        return sum_num == aim
    return isSum(arr, i + 1, sum_num, aim) or isSum(arr, i + 1, sum_num + arr[i], aim)


# res = isSum([3, 2, 7, 12], 0, 0, 13)
# print(res)


def isSum2(arr, i, sum_num, aim):
    col = range(sum(arr))  # 代表列数
    row = range(len(arr) + 1)  # 代表行数
    multilist = [[False for _ in col] for _ in row]
    multilist[len(arr)][aim] = True
    # print(multilist)
    for i in range(len(arr) - 1, -1, -1):
        for j in col:
            multilist[i][j] = multilist[i + 1][j]
            try:
                multilist[i][j] = (multilist[i][j] or multilist[i + 1][j + arr[i]])
            except:
                pass
    print(multilist)
    return multilist[i][sum_num]


test = isSum2([3, 2, 5], 0, 0, 7)
print(test)