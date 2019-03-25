# lists = [3, 5, 4, 2, 1, 6]


def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2  # L和R中点的位置
    listA = MergeSort(lists[:middle])  # T(n/2)
    listB = MergeSort(lists[middle:])  # T(n/2)
    return MergeSortedLists(listA, listB)  # O(n)
    # master: T(n) = 2T(n/2) + O(n)
    # 时间复杂度: O(N*logN)


def MergeSortedLists(listA, listB):
    help_list = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] <= listB[b]:
            help_list.append(listA[a])
            a += 1
        else:
            help_list.append(listB[b])
            b += 1
    help_list.extend(listA[a:])
    help_list.extend(listB[b:])
    # while a < len(listA):
    #     help_list.append(listA[a])
    #     a += 1
    #
    # while b < len(listB):
    #     help_list.append(listB[b])
    #     b += 1
    return help_list


if __name__ == '__main__':
    lists = [3, 5, 4, 2, 1, 6, 9, 11, 0, 10, 1]
    result = MergeSort(lists)
    print(result)
