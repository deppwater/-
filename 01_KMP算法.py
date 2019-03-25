"""
目的：
给一个字符串str1和字符串str2
str1 = 'abkababkabf……'
str2 = 'abkababkabt'
实现一个算法，如果字符串str1中含有子串str2
则返回str2在str1中的开始位置。不含有则返回-1.

算法思路：
暴力的笨方法是从str1的第一位开始 只要匹配上了str2的第一位
那么就继续看后面的每一位是否能与str2对应上 只要遇到不匹配 那么str1向后挪一位
kmp算法：
准备一个列表 里面放对应str2每一位之前的字符最大(前缀与后缀相等)的长度
规定第一位由于之前没有字符 所以存-1  第二位存0
从第三位开始 例如str2对应的列表为：
[-1, 0, 0, 0, 1, 2, 1, 2, 3, 4, 5]
匹配过程：
假设出现上面匹配到str2的最后一位出现了不匹配的情况 此时str1的指针指在f str2的指在t
那么str1的指针不动 str2的指针指向此时t对应在列表位置上的数对应的位置即5位置
也就意味着相当于str2向右移动5个位置 此时的情况为：
str1 = 'abkababkabf……'
str2 =      'abkababkabt'
因为有最大前缀与后缀相等的一个范围 那么代表此时两个指针之前的字符都是一一匹配的
所以就可以从新的指针指的位置开始匹配
如果再发现遇到不相等的时候 重复上述的操作 即此时需要移动到str2指针指向的字符在列表中对应的数所对应的位置即2上：
str1 = 'abkababkabf……'
str2 =         'abkababkabt'
然后继续进行上述操作
"""


"""
使用KMP算法快速解决字符串匹配问题：
1.首先生成match字符串的nextArr数组，这个数组的长度与match字符串的长度一样，
nextArr[i]的含义是在match[i]之前的字符串match[0...i-1]中，必须以match[i-1]结尾的后缀子串（不能包含match[0]）
与必须以match[0]开头的前缀子串（不能包含match[i-1]）最大的匹配长度是多少。这个长度就是nextArr[i]的值。
2.假设从str[i]字符出发时，匹配到j位置的字符发现与match中的字符不一致。也就是说，str[i]与match[0]一样，
并且从这个位置开始一直可以匹配，即str[i,,,j-1]与match[0...,j-i-1]一样，知道发现str[j]!=match[j-1]，
匹配停止。因为现在已经有了match字符串的nextArr数组，nextArr[j-1]的值表示match[0...j-i-1]这一段字符串前缀和后缀的最大匹配。
下一次直接让str[j]与match[k]进行匹配检查。对于match来说，相当于向右滑动，让match[k]滑动太str[j]同一个位置上，
然后进行后续的匹配检查。直到在str的某一个位置把match完全匹配完，就说明str中有match。如果match滑到最后也没有匹配出来，就说明str中没有match.
3.匹配过程分析完毕，str中匹配的位置是不退回的，match则一直向右滑动，如果在str中的某个位置完全匹配出match，
整个过程停止。否则match滑到str的最右侧过程也停止，所以滑动的长度最大为N，所以时间复杂度为O(N)。
"""


def getNextArr(string):
    if len(string) == 1:
        return [-1]
    # 准备一个与string等长的数组
    next_arr = [0] * len(string)
    # 默认第一位为-1 第二位为0
    next_arr[0] = -1
    next_arr[1] = 0
    # i为当前起始位置 cn为当前前一位的next数组的值
    i = 2
    cn = 0
    while i < len(next_arr):
        # 比较当前位置i 的前一位 对应在string中的数
        # 与i的前一位的最长前缀 对应在string中的数
        # 如果两者相等则代表i的最长前缀为 cn+1
        if string[i - 1] == string[cn]:
            cn += 1
            next_arr[i] = cn
            i += 1
        # 此时是不相等的情况 修改最长前缀的值为cn位置对应的next数组的值 相当于折半并重新判断
        # 需要注意的是cn在下一轮比较时不更新的原因是如果更新则代表上一步计算有误
        elif cn > 0:
            cn = next_arr[cn]
        # 如果折半到没法再折半代表没有相等的部分 直接赋值0
        else:
            next_arr[i] = 0
            i += 1
    return next_arr


# next_Arr = getNextArr('abkababkabt')
# print(next_Arr)


def getIndexOf(string, match):
    if not string or not match or len(match) < 1 or len(string) < len(match):
        return -1
    ss = string
    ms = match
    nextArr = getNextArr(match)
    si = 0
    mi = 0
    while si < len(ss) and mi < len(ms):
        if ss[si] == ms[mi]:
            si += 1
            mi += 1
        elif nextArr[mi] == -1:
            si += 1
        else:
            mi = nextArr[mi]
    return si - mi if mi == len(ms) else -1


res = getIndexOf('sdfaabkababkabtsdaw', 'abkababkabt')
# res2 = getNextArr('abkababkabt')

print(res)
# print(res2)


"""
面试题原题：
给定一个字符串 在这个字符串后面添加字符串
要求添加的字符串长度最短且能补出一个完整的原字符串
例如： 'abcabc'
需要补的最短字符串为： 'abc'
"""


def getNext(arr):
    if len(arr) == 1:
        return [-1]
    nextArr = [0] * (len(arr) + 1)
    nextArr[0] = -1
    nextArr[1] = 0
    index = 2
    cn = 0
    while index < len(arr) + 1:
        if arr[index - 1] == arr[cn]:
            cn += 1
            nextArr[index] = cn
            index += 1
        elif cn > 0:
            cn = nextArr[cn]
        else:
            nextArr[index] = 0
            index += 1
    print(nextArr)
    min_num = nextArr[-1]
    return arr[min_num:]


res = getNext('ccbcc')
print(res)

"""
面试题：
如何求一个树结构是否完全是另一个数的子树
此处另一个树的任意一个子树必须包含所有该头结点的子节点
如： 1   的子树不能是： 1
   / \             /
  1   1           1
思路：
先求出两个树的序列化的结果 再判断是否包含
"""

"""
面试题：
如何确定一个字符串是不是由一个范式决定的
"""


def judgeNum(arr):
    if len(arr) == 1:
        return [-1]
    help_li = [0] * (len(arr) + 1)
    help_li[0] = -1
    help_li[1] = 0
    index = 2
    cn = 0
    while index < len(arr) + 1:
        if arr[index - 1] == arr[cn]:
            cn += 1
            help_li[index] = cn
            index += 1
        elif cn > 0:
            cn = help_li[cn]
        else:
            help_li[index] = 0
            index += 1
    help_li.reverse()
    end_index = help_li.index(0)
    # print(end_index)
    length_li = len(help_li)
    # print(help_li)
    for i in range(end_index - 1):
        if help_li[i] - help_li[i + 1] != 1:
            return False
    if (length_li - 1) % (length_li - 1 - end_index) == 0 and end_index != 0:
        # print(length_li - 1)
        # print(length_li - 1 - end_index)
        return True
    return False


res = judgeNum([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4])
res2 = judgeNum([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
res3 = judgeNum([1, 2, 3, 4, 5, 1, 2, 3, 4])
print(res)
print(res2)
print(res3)
