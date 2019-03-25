# 设计RandomPool结构
# 【题目】 设计一种结构，在该结构中有如下三个功能：
# insert(key)：将某个key加入到该结构，做到不重复加入。
# delete(key)：将原本在结构中的某个key移除。 getRandom()：
# 等概率随机返回结构中的任何一个key。
# 【要求】 Insert、delete和getRandom方法的时间复杂度都是
# O(1)
import random


class RandomPool(object):
    def __init__(self):
        self.map1 = {}
        self.map2 = {}
        self.size = -1

    def add(self, string):
        self.size += 1
        self.map1[string] = self.size
        self.map2[self.size] = string

    def delete(self, string):
        # print(self.map2[self.map1[string]])
        # print(self.map2[self.size])
        help_index = self.map1[string]
        self.map2[help_index] = self.map2[self.size]
        self.map1.pop(string)
        self.map2.pop(self.size)
        self.size -= 1
        self.map1[self.map2[help_index]] = help_index

    def getRandom(self):
        ran_index = random.randint(0, self.size)
        return self.map2[ran_index]


text = RandomPool()
text.add('1')
text.add('2')
text.add('3')
text.add('4')
text.add('5')
text.delete('3')
# print(text.size)
print(text.map2)
print(text.map1)
# print(text.map2[3])
res = text.getRandom()
print(res)
