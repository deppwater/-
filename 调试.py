# class test:
#     def __init__(self, test_num):
#         self.test_num = test_num
#
#     def plus(self):
#         self.test_num += 1
#
# demo = test(1)
# demo.plus()
# print(demo.test_num)

# a = ['职场', ' 1 评论 ', '开发', '面试']
#
# b = [element for element in a if not element.strip().endswith("评论")]
# print(b)
#
# c = "-".join(b)
# print(c)
import  copy


a = [1, 2, 3]
b = a[:]
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))
