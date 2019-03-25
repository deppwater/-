# 给定一个数组，求如果排序之后，相邻两数的最大差值，要求时间复杂度O(N)，且要求不能用非基于比较的排序。

"""
思路：
假设数组长度为N 准备N+1个桶 即0号桶到N号桶
遍历数组 将该数组的最小值放在0号桶 最大值放在N号桶 那么必然至少存在一个空桶
然后再将数组中的数分别放在对应的桶内 每个桶内有自己的最大值和最小值
当有一个新的数进入桶内的时候 只跟最大值和最小值比较 处在中间的数不做记录
由于这个空桶的存在 整个数组的相邻数的最大差值必然存在于相邻两个非空桶的最大值和最小值
为什么不直接找空桶两侧的桶比较 是因为两个相邻非空桶如果左边桶取范围内最小值 右边桶取范围内最大值 两者差值要大于空桶两侧的差值
设计这个必有一个空桶的分析方式只是为了否定来自桶内部的可能性
代码构建：
准备三个数组 长度都为N+1 以及三个变量
数组max_li 用来记录每个桶的最大值
数组min_li 用来记录每个桶的最小值
数组boolean 用来记录每个桶中是否有值
变量max_num 用来记录整个数组的最大值
变量min_num 用来记录整个数组的最小值
变量length 用来记录整个数组的长度
根据max_li和min_li建立桶
遍历数组 根据每个数的值数组长度以及max_li与min_li确定该数应放在哪个桶 那么那个桶的对应位置的三个数值都要进行更新
然后再次进行遍历 过程中求出每一个非空桶的min_li与前一个非空桶的max_li的差值的最大值
"""


# 方法一
def ArrayStack(lists):
    length = len(lists)
    # dic = dict.fromkeys(range(length + 1), [])
    dic = dict()
    for i in range(length):
        dic[i] = list()
        print(dic)
    return AddNumbers(dic, lists, length)


def AddNumbers(dic, lists, length):
    min_num = min(lists)
    max_num = max(lists)
    # print(dic[0])
    # print(length)
    dic[0] = [min_num]
    # print(dic)
    dic[length] = [max_num]
    # print(dic)
    # print(dic)
    lists.remove(min_num)
    lists.remove(max_num)
    # print(lists)

    for i in lists:
        index = int(i * length / (min_num + max_num) - 1)
        # print('='*50)
        # print(dic)
        # print(dic[index])
        length_dict = len(dic[index])
        if length_dict == 0:
            dic[index] = [i]
        elif length_dict == 1:
            if i > dic[index][0]:
                dic[index].insert(1, i)
            elif i < dic[index][0]:
                dic[index].insert(0, i)
            else:
                continue
        elif length_dict == 2:
            if i < dic[index][0]:
                dic[index][0] = i
            elif i > dic[index][1]:
                dic[index][1] = i
            else:
                continue
    return DealNumbers(dic, length)


def DealNumbers(dic, length):
    peek_num_list = list()
    key_list = list()
    for i in range(length + 1):
        if not dic[i]:
            dic.pop(i)

    for i in dic:
        key_list.append(i)
    # print(key_list)
    new_length = len(dic)
    # print(dic)
    for i in range(new_length - 1):
        peek_num_list.append(min(dic[key_list[i + 1]]) - max(dic[key_list[i]]))
    # print(peek_num_list)
    return max(peek_num_list)


# if __name__ == '__main__':
#     result = ArrayStack([9, 2, 3, 4, 7, 11, 21, 12, 15, 31])
#     print(result)


# 方法二：
def maxGap(arr):
    if arr is None or len(arr) < 2:
        return 0
    max_num = max(arr)
    min_num = min(arr)
    len_arr = len(arr)
    if max_num == min_num:
        return 0
    max_li = [[]] * (len_arr + 1)
    min_li = [[]] * (len_arr + 1)
    boolean = [[]] * (len_arr + 1)
    for i in range(len_arr):
        bid = bucket(arr[i], len_arr, min_num, max_num)
        # print(bid)
        max_li[bid] = arr[i] if not max_li[bid] else max(max_li[bid], arr[i])
        min_li[bid] = arr[i] if not min_li[bid] else min(min_li[bid], arr[i])
        boolean[bid] = True
    print(max_li)
    print(min_li)
    # print(boolean)
    res = 0
    last_max = 0
    for i in range(len_arr + 1):
        if boolean[i]:
            res = max((min_li[i] - last_max), res)
            last_max = max_li[i]
    print(res)


def bucket(num, len_arr, min_num, max_num):
    return int((num - min_num) * len_arr / (max_num - min_num))

maxGap([9, 2, 3, 4, 7, 11, 21, 12, 15, 22])
print(sorted([9, 2, 3, 4, 7, 11, 21, 12, 15, 31]))

