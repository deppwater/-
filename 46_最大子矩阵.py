"""
给定一个整形矩阵map 其中的值只有0和1 求其中全是1的所有矩形区域中 最大区域包含1的个数
如：
1 1 1 0
其中 最大矩阵有3个1 返回3
如：
1 0 1 1
1 1 1 1
1 1 1 0
其中 最大矩阵有6个1 返回6
"""

"""
思路：
这个问题就可以转化为：
拿上面的例子来说 一共有3行
分别以第0、1、2行为底 向上看有多少个连续的1
例如以第1行为底就可以得到一个数组：[1,0,1,1]
第2行为底：[2,1,2,2]
第3行为底：[3,2,3,0]
问题就转化成给定直方图高度求最大矩阵的问题了
那么此时的时间复杂度为O(M*N)
"""

import queue


def change(matrix):
    row = len(matrix)
    col = len(matrix[0])
    helpColArr = [i for i in range(col)]
    helpArr = [0] * col
    helpOutput = []
    helpRemove = []
    # 将矩阵变为以每一行为底的直方图
    for i in range(row):
        # print(helpColArr)
        while i != -1:
            for j in helpColArr:
                # print(matrix[i][j])
                if matrix[i][j] == 1:
                    helpArr[j] += 1
                    # print(j)
                else:
                    helpRemove.append(j)
            # 这里要注意不能边修改边删除 必须先加入删除队列再单独删除
            for k in helpRemove:
                helpColArr.remove(k)
            i -= 1
            helpRemove = []
        helpOutput.append(helpArr)
        print(helpArr)
        helpColArr = [i for i in range(col)]
        helpArr = [0] * col
    for arr in helpOutput:
        maxRecFromBottom(arr)
    maxRecFromBottom([4, 2, 6, 7, 6])
    return helpOutput


def maxRecFromBottom(highArr):
    maxArea = 0
    helpQueue = queue.LifoQueue()
    # helpQueue里需要存的是坐标而不是值
    helpQueue.put(0)
    # helpIndex = 0
    for i in range(1, len(highArr)):
        curIndex = helpQueue.get()
        helpQueue.put(curIndex)
        # print(len(highArr))
        # print('help')
        # 单调栈从底部到顶部为由小到大 所以遇到新加入的数小于等于当前栈顶的数的时候需要弹出
        while not helpQueue.empty() and highArr[i] <= highArr[curIndex]:
            j = helpQueue.get()
            if helpQueue.empty():
                k = -1
            else:
                k = helpQueue.get()
                # helpIndex = k
                # 这种情况需要更新一下curIndex 不然会跟一个已经弹出的数据进行比较
                curIndex = k
                helpQueue.put(k)
            curArea = (i - k - 1) * highArr[j]
            # helpQueue.put(j)
            # print(curArea)
            maxArea = max(maxArea, curArea)
        helpQueue.put(i)
        # print(helpIndex)

    # print(helpIndex)
    # 现在的情况是如果没有相同的数字可以正常运行 如果有相同的数字边界会出错
    # 相等的情况可能得分开考虑
    # if helpQueue.qsize() > 1:
    #     while not helpQueue.empty():
    #         j = helpQueue.get()
    #         if helpQueue.empty():
    #             k = -1
    #         else:
    #             k = helpQueue.get()
    #         curArea = (len(highArr) - k - 1) * highArr[j]
    #         maxArea = max(maxArea, curArea)
    # else:
    #     j = helpQueue.get()
    #     curArea = ((len(highArr)) - helpIndex - 1) * highArr[j]
    #     maxArea = max(maxArea, curArea)
    # print(maxArea)

    while not helpQueue.empty():
        j = helpQueue.get()
        if helpQueue.empty():
            k = -1
        else:
            k = helpQueue.get()
            helpQueue.put(k)
        curArea = (len(highArr) - k - 1) * highArr[j]
        maxArea = max(maxArea, curArea)
    print(maxArea)


change([[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]])
# print(res)
