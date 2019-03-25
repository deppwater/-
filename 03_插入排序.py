def insert_sort(alist):
    """
    插入排序：
    假设数组第一个数为有序的
    拿数组第二个数插入当前的有序数组 以此类推
    与选择排序的区别在于选择排序操作的是右边的数组 插入排序操作的是左边的

    时间复杂度 ------- O(n^2)
    最优时间复杂度 ---- O(n)
    平均时间复杂度 ---- O(n^2)
    所需辅助空间 ------ O(1)
    稳定性 ------------ 稳定
    :return:
    """
    """
    如果比较操作的代价比交换操作大的话
    可以采用二分查找法来减少比较操作的次数
    称为二分插入排序
    """
    n = len(alist)
    j = 2
    while j < n:
        k = j
        for i in range(j, 0, -1):
            if alist[k] < alist[k - 1]:
                alist[k], alist[k - 1] = alist[k - 1], alist[k]
                k -= 1
            else:
                break
        j += 1
    return alist


list1 = [8, 11, 3, 5, 2, 1, 9, 7, 4]
result = insert_sort(list1)
print(result)