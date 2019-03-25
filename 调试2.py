a = [1, 5, 2, 3, 1]
b = [1] * len(a)
print(type(set(a)))
c = list(set(b) ^ set(a))
c.sort(key=a.index)
print(c[-1])

# a = {'xiaoming': 80, 'huang': 60, 'zi': 70}
#
# res = sorted(a.items(), key=lambda x: x[1])
# print(res)

list1 = [{"a": 3}, {"b": 2}, {"c": 1}]
# print(list(list1[0].keys())[0])
res = sorted({list(list1[x].keys())[0]: list(list1[x].values())[0] for x in range(3)}.items(), key=lambda x: x[1])
print(res)


# print(id(id(c)))
# print(id(c))
class Test(object):
    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age

    @property
    def age(self):
        return self.__age


test = Test()
print(test.age)
