"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        help_nums = nums[:]
        help_nums.sort()
        node1_index = 0
        node2_index = len(nums) - 1
        while (help_nums[node1_index] + help_nums[node2_index]) != target:
            if help_nums[node1_index] + help_nums[node2_index] < target:
                node1_index += 1
            else:
                node2_index -= 1

        n1 = nums.index(help_nums[node1_index])
        nums.reverse()
        n2 = len(nums) - 1 - nums.index(help_nums[node2_index])
        return [n1] + [n2]


test = Solution()
res = test.twoSum([3, 3, 3], 6)
print(res)