# 给定一个数组arr，和一个数num，请把小于num的数放在数组的左边，等于num的数放在数组的中间，大于num的数放在数组的右边
# 要求额外空间复杂度O(1)，时间复杂度O(N)

"""
思路：
准备三个指针less和more less起始在-1位置 more起始在数组长度+1的位置 cur起始在0位置
遍历数组 判断cur位置的数与num的大小
当cur<num的时候 将cur所指的数与less的下一个位置交换 cur+=1 less+=1
当cur=num的时候 less不动 cur继续向右移动 即cur+=1
当cur>num的时候 将cur所指的数与more的前一个位置交换 但cur不动 less-=1 然后继续判断cur位置的新数
当cur与more指针相遇的时候 结束循环

稳定性 ----------- 不稳定
"""


def holland(lists, num):
    less = -1
    more = len(lists)
    cur = 0
    while cur < more:
        if lists[cur] < num:
            lists[cur], lists[less + 1] = lists[less + 1], lists[cur]
            less += 1
            cur += 1
        elif lists[cur] > num:
            lists[cur], lists[more - 1] = lists[more - 1], lists[cur]
            more -= 1
        else:
            cur += 1
        if cur == more:
            return lists


if __name__ == '__main__':
    result = holland([2, 4, 10, 5, 11, 6, 8, 5, 0, 3, 5, 1, 9, 7], 5)
    print(result)
