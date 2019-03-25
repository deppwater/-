def quick_sort_ver1(alist, start, end):
    """
    快速排序：
    一般以最后一个数作为基准数 整体上小的放在左边大的放在右边 然后进行递归操作
    详细过程为 构造两个指针 Left和Right
    Left开始指在坐标为0的位置 比较和基准数的大小
    如果比基准数小 Left指针向右移动
    如果比基数大 则把此时Left所指的给Right现在所指的位置即基数所在的最后一位 此时Left所指的位置为None
    如果进行了上述操作则换Right指针开始向左移动 Left指针不动 指向None
    如果比基数大 Right指针向左移动
    如果比基数小 则把Right所指位置交给Left 此时Right所指位置为None
    当Left与Right指针相撞时插入基准数 然后递归进行上述操作

    时间复杂度 ------- O(n^2)
    最优时间复杂度 ---- O(nlogn)
    平均时间复杂度 ---- O(nlogn)
    所需辅助空间 ------ O(logn)~O(n)
    稳定性 ----------- 不稳定
    :return:
    """
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort_ver1(alist, start, low - 1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort_ver1(alist, low + 1, end)


list1 = [8, 11, 3, 14, 15, 5, 2, 1, 9, 7, 4, 13, 6, 10]
quick_sort_ver1(list1, 0, len(list1) - 1)
print(list1)


def quick_sort_ver2(alist):
    """
    递归快速排序(伪快排)
    :return:
    """
    if len(alist) < 2:
        return alist
    else:
        mid_value = alist[-1]
        lList = [i for i in alist[:-1] if i <= mid_value]
        rList = [i for i in alist[:-1] if i > mid_value]
        return quick_sort_ver2(lList) + [mid_value] + quick_sort_ver2(rList)
