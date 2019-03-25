import extra


def select_sort(alist):
    """
    选择排序：
    从头开始遍历数组
    每次找到需要排序数组的最小的值与需要排序数组的第一位交换
    需要排序数组的长度每次减少一

    时间复杂度 -------- O(n^2)
    最优时间复杂度 ---- O(n^2)
    平均时间复杂度 ---- O(n^2)
    所需辅助空间 ------ O(1)
    稳定性 ----------- 不稳定
    :return:
    """
    n = len(alist)
    j = 0
    while j < n - 1:
        min_index = j
        for i in range(j, n):
            if alist[i] < alist[min_index]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
        j += 1
    return alist


# list1 = [8, 11, 3, 5, 2, 1, 9, 7, 4]
# result = select_sort(list1)
# print(result)

extra.Testing.mainTest(10000, select_sort)
