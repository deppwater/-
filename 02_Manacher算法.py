# 给定一个字符串str，返回str中最长回文子串的长度。
# 例如：
# str="123"，其中的最长回文子串为“1”、“2”或者“3”，所以返回1.
# str="abc1234321ab"，其中最长回文子串为“1234321”,所以返回7.


"""
常规方法思路：
不论是奇回文还是偶回文 给每个字符之间以及字符串开头和结尾增加一个#符号
算出包括#符号在内每一位向两边扩的最大长度 然后讲这个数字//2就是要求的回文数
例如： 11311  可以变成： #1#1#3#1#1#
求出每一位的最大回文数为： 13531(11)13531
那么这个字符串最大回文子串的长度为： 11/2 = 5
常规算法的复杂度为O(N^2)


Manacher算法：
回文直径与回文半径：
一个字符向两边扩的最大长度与最大长度的一半
回文半径数组：
将回文半径组成一个数组 但在过程中要考虑是否能用之前得出的回文半径
回文右边界：
在从左向右确定回文直径的过程中 过程中向右扩的最远点为回文右边界
回文右边界的中心：
取得回文右边界的那个字符所在的位置 可能不是回文右边界的一半

可能性：
1.要扩的位置不在回文右边界里 那么暴力扩边界
2.要扩的位置在回文右边界里：
   1.先找出要求的i位置关于第一次到达当前回文右边界的c点对应的点i'
     然后可以的出i'位置的回文直径 如果i'的回文直径在c的回文直径之内
     那么i的回文直径即为i'的回文直径 （复杂度：O(1)）
   2.如果i'的回文直径超过了c的回文直径的左边界
     那么i的回文半径为i到c的回文直径的右边界 （复杂度：O(1)）
   3.如果i'的回文直径的左边界与c的回文直径的左边界重叠了
     当然i'的回文右边界不一定在c点 那么i的回文直径要从c的回文直径的右边界开始继续尝试扩大
复杂度：
不论是情况1还是情况2里的情况3 回文右边界最终只会扩大到N
Manacher算法的时间复杂度为O(N)。关键之处在于估算扩出去检查这一行为发生的数量。原字符串在处理后的长度由N变为2N。
要么在计算一个未知的回文半径时完全不需要扩出去检查，要么每一次扩出去检查都会导致pR变量的更新。扩出去检查时都让回文半径到达更右的位置，
当然会使pR更新。然而pR最多是从-1增加到2N（右边界），并且从不减少，所以扩出去检查的次数就是O(N)级别的。所以Manacher算法的时间复杂度为O(N)。
"""


# def Manacher(string):
#     if len(string) == 1:
#         return [1]
#     # 先给数组的每个数中间和结尾加上#字符
#     new_string = '#'.join(string)
#     new_string = '#' + new_string + '#'
#     # 准备一个记录对应每个位置的回文长度的数组
#     plalindrome_li = [1] * len(new_string)
#     plalindrome_li[0] = 1
#     plalindrome_li[1] = 3
#     # 准备最大回文长度的右边界
#     right_index = 2
#     pre_index = 2
#     # 记录第一次到达最大回文右边界的点的位置
#     c = 1
#     while pre_index < len(plalindrome_li):
#         # 回文直径
#         print(plalindrome_li)
#         print('test2')
#         diam = 1
#         if pre_index > right_index:
#             help_index = pre_index
#             i = 1
#             print('test')
#             # if help_index - i - 1 >= 0 and help_index + i + 1 <= len(new_string) - 1:
#             try:
#                 while new_string[help_index - i] == new_string[help_index + i]:
#                     diam += 2
#                     i += 1
#             except:
#                 pass
#             plalindrome_li[pre_index] = diam
#             right_index = pre_index + plalindrome_li[pre_index] // 2
#             pre_index += 1
#
#         else:
#             # 求pre_index关于c的对称点
#             # 第2种情况的情况1
#             diam = 0
#             c = right_index // 2
#             symmetry_point = c * 2 - pre_index
#             if plalindrome_li[symmetry_point] < (plalindrome_li[c] // 2) + 1:
#                 plalindrome_li[pre_index] = plalindrome_li[symmetry_point]
#                 pre_index += 1
#             elif plalindrome_li[symmetry_point] > (plalindrome_li[c] // 2) + 1:
#                 plalindrome_li[pre_index] = (right_index - pre_index) * 2 + 1
#                 pre_index += 1
#             else:
#                 i = right_index - pre_index + 1
#                 help_index = pre_index
#                 while new_string[help_index - i] == new_string[help_index + i]:
#                     if help_index - i >= 0 and help_index + i < len(new_string):
#                         diam += 2
#                         i += 1
#                     else:
#                         break
#                 plalindrome_li[pre_index] = diam + (right_index - pre_index) * 2 + 1
#                 right_index += diam // 2
#                 pre_index += 1
#     return plalindrome_li
#
#
# res = Manacher('aaaaa')
# print(res)


def Manacher(string):
    if string is None or len(string) == 0:
        return -1
    # 先给数组的每个数中间和结尾加上#字符
    new_string = '#'.join(string)
    new_string = '#' + new_string + '#'
    # 准备一个记录对应每个位置的回文长度的数组
    pArr = [1] * len(new_string)
    # 第一次抵达最大右边界的坐标
    index = -1
    # 回文右边界
    pR = -1
    for i in range(len(pArr)):
        # 首先最大右边界只可能大于或等于当前坐标
        # 这个式子的意思是如果最大右边界等于当前坐标则当前坐标的最大回文半径为1 即以自身为半径和直径
        # 如果最大右边界大于当前坐标值
        # (pArr[2 * index - i])为i关于index的对称点   (pR - i)为最大右边界距离i的长度
        # 如果后者小于前者那么按思路里来直接给pArr[i]赋值为后者即可
        # 如果相等需要给pArr[i]赋值为前者并继续进行比较
        # 这里多了一步对于前面的情况的判断 不影响结果
        # print((pArr[2 * index - i], pR - i))
        pArr[i] = min(pArr[2 * index - i], pR - i) if pR > i else 1
        while i + pArr[i] < len(new_string) and i - pArr[i] > -1:
            if new_string[i + pArr[i]] == new_string[i - pArr[i]]:
                pArr[i] += 1
            else:
                break
        # 如果当前节点坐标+当前节点的最大回文半径>当前记录的最大回文半径 那么更新最大回文半径和到达这个回文半径的坐标值
        if i + pArr[i] > pR:
            pR = i + pArr[i]
            index = i
            # max = min(max, pArr[i])
    return pArr


res = Manacher('aacca')
# #a#a#c#a#
# print(res)

"""
进阶题目：给定一个字符串str，想通过添加字符的方式使得str整体都变成回文字符串，但要求只能在str的末尾添加字符
请返回在str后面添加的最短字符串。

例如：str="12"。在末尾添加“1”之后，str变成“121”,是回文串。在末尾添加“21”之后
str变成“1221”,也是回文串，但“1”是所有添加方案中最短的，所以返回“1”。

思路：
问题可以转化为
先求在必须包含最后一个字符的前提下最大的回文字符串长度
那么左边剩下的再逆序添加到末尾即可
"""


def makePlalindrome(string):
    if string is None or len(string) == 0:
        return -1
    new_string = '#'.join(string)
    new_string = '#' + new_string + '#'
    # print(new_string)
    Plalindrome_li = [1] * len(new_string)
    # 到达当前最大回文右边界的半径点对应的坐标
    index = -1
    # 当前最大回文右边界
    pR = -1
    for i in range(len(new_string)):
        Plalindrome_li[i] = min(Plalindrome_li[index * 2 - i], pR - i) if pR > i else 1
        # 开始暴力找最大回文半径
        while i + Plalindrome_li[i] < len(new_string) and i - Plalindrome_li[i] > -1:
            if new_string[i + Plalindrome_li[i]] == new_string[i - Plalindrome_li[i]]:
                Plalindrome_li[i] += 1
            # 当某一次找某个点的最大回文半径的时候碰到了右边界 因为是从左往右找的 所以一旦碰到就可以停止了
            else:
                break
        if i + Plalindrome_li[i] == len(new_string):
            break
        # 更新最大回文半径
        if i + Plalindrome_li[i] > pR:
            pR = i + Plalindrome_li[i]
            index = i
    help_li = Plalindrome_li
    help_li.reverse()
    j = 0
    print(Plalindrome_li)
    while help_li[j] == 1 and j < len(help_li) - 1:
        j += 1
    last_num = help_li[j]
    if Plalindrome_li.index(last_num) % 2 == 0:
        # print(Plalindrome_li)
        return string[:len(string) - (last_num // 2) * 2][::-1]
    else:
        return string[:len(string) - (last_num // 2) * 2 + 1][::-1]

string = 'abcd'
res1 = makePlalindrome(string)
print(res1)
print(string)