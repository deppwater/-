# import copy

# a = [1,2]
# b = [3,4]
# c = [a,b]
# d = copy.copy(c)
# e = copy.deepcopy(c)
# print(id(c))
# print(id(d))
# print(id(e))
# print(id(c[0]))
# print(id(d[0]))
# print(id(e[0]))


# a2 = (1, 2, 3)
# b2 = copy.copy(a2)
# c2 = copy.deepcopy(a2)
# print(id(a2))
# print(id(b2))
# print(id(c2))


# a = [1, 2, 3]
# b = copy.copy(a)
# c = copy.deepcopy(a)
# print(id(a))
# print(id(b))
# print(id(c))
# a.append(4)
# print(b)
# print(c)


# a = {'value': [1, 2, 3, 4]}
# b = a.copy()
# c = copy.deepcopy(a)
# print(id(a))
# print(id(b))
# print(id(c))
# a['value'].append(5)
# print(b)
# print(c)



# a = 'value'
# b = copy.copy(a)
# c = copy.deepcopy(a)
# print(id(a))
# print(id(b))
# print(id(c))


# print("******多继承使用super().__init__ 发生的状态******")
#
#
# class Parent(object):
#     def __init__(self, name):  # 为避免多继承报错，使用不定长参数，接受参数
#         print('parent的init开始被调用')
#         self.name = name
#         print('parent的init结束被调用')
#
#
# class Son1(Parent):
#     def __init__(self, name, age):  # 为避免多继承报错，使用不定长参数，接受参数
#         print('Son1的init开始被调用')
#         self.age = age
#         Parent.__init__(self, name)  # 为避免多继承报错，使用不定长参数，接受参数
#         print('Son1的init结束被调用')
#
#
# class Son2(Parent):
#     def __init__(self, name, gender):  # 为避免多继承报错，使用不定长参数，接受参数
#         print('Son2的init开始被调用')
#         self.gender = gender
#         Parent.__init__(self, name)  # 为避免多继承报错，使用不定长参数，接受参数
#         print('Son2的init结束被调用')
#
#
# class Grandson(Son2, Son1):
#     def __init__(self, name, age, gender):
#         print('Grandson的init开始被调用')
#         # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
#         # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
#         # super(Grandson, self).__init__(name, age, gender)
#         Son2.__init__(self, name, gender)
#         Son1.__init__(self, name, age)
#
#         # super().__init__(name, age, gender)
#         print('Grandson的init结束被调用')
#
#
# print(Grandson.__mro__)
#
# gs = Grandson('grandson', 12, '男')
# print('姓名：', gs.name)
# print('年龄：', gs.age)
# print('性别：', gs.gender)
# print("******多继承使用super().__init__ 发生的状态******\n\n")
import hashlib


# def main():
#     # 创建Connection连接
#     conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='123456', charset='utf8')
#     # 获得Cursor对象
#     cursor = conn.cursor()
#     # 插入10万次数据
#     for i in range(100000):
#         cursor.execute("insert into test_index values('ha-%d')" % i)
#     # 提交数据
#     conn.commit()
#
#
# if __name__ == "__main__":
#     main()

def md5_key(arg):
    hash = hashlib.md5()
    hash.update(arg)
    return hash.hexdigest()

res = md5_key('www.yahuoo.com'.encode())
print(res)
print(int(res[:16], 16))
print(len('11549998973798585840'))