def shell_sort(alist):
    """
    希尔排序：
    每次以不同的步长对数组进行分组 然后进行分组的插入排序
    减少步长 重复上面的操作 直到数组有序
    区别在于希尔排序可以让元素向最终位置更快的移动

    时间复杂度 ------- O(n^2)
    最优时间复杂度 ---- 根据步长序列的不同而不同
    平均时间复杂度 ---- 根据步长序列的不同而不同。
    所需辅助空间 ------ O(1)
    稳定性 ----------- 不稳定
    :return:
    """
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap + 1, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - 1]:
                    alist[i], alist[i - 1] = alist[i - 1], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist


list1 = [8, 11, 3, 14, 15, 5, 2, 1, 9, 7, 4, 13, 6, 10]
result = shell_sort(list1)
print(result)